package main

import (
	"log"
	"net/http"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"

	"github.com/CS331-06-BusinessAutomation/backend/auth/internal/cleanup"
	"github.com/CS331-06-BusinessAutomation/backend/auth/internal/config"
	"github.com/CS331-06-BusinessAutomation/backend/auth/internal/database"
	"github.com/CS331-06-BusinessAutomation/backend/auth/internal/handler"
)

func main() {
	// Load configuration
	cfg, err := config.Load()
	if err != nil {
		log.Fatalf("Failed to load config: %v", err)
	}

	// Connect to Supabase PostgreSQL
	if err := database.Connect(cfg.DatabaseURL); err != nil {
		log.Fatalf("Failed to connect to database: %v", err)
	}

	// Run migrations
	if err := database.Migrate(); err != nil {
		log.Fatalf("Failed to run migrations: %v", err)
	}

	// Start cleanup background job (runs every 5 min, deletes soft-deleted records older than 30 days)
	cleanup.Start(cleanup.DefaultConfig())

	// Initialize handlers
	webhookHandler := handler.NewWebhookHandler(cfg.ClerkWebhookSecret)

	// Set Gin to release mode (less verbose logging)
	gin.SetMode(gin.ReleaseMode)

	// Create Gin router with logging and recovery
	r := gin.New()
	r.Use(gin.Logger()) // Shows HTTP status codes
	r.Use(gin.Recovery())

	// CORS configuration
	r.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"*"}, // Configure for production
		AllowMethods:     []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowHeaders:     []string{"Accept", "Authorization", "Content-Type"},
		ExposeHeaders:    []string{"Link"},
		AllowCredentials: true,
		MaxAge:           300,
	}))

	// Health check
	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok"})
	})

	// Webhook endpoint (no auth required)
	r.POST("/api/webhooks/clerk", webhookHandler.Handle)

	// Start server
	addr := ":" + cfg.Port
	log.Printf("Auth service running on http://localhost%s", addr)

	if err := r.Run(addr); err != nil {
		log.Fatalf("Server failed: %v", err)
	}
}
