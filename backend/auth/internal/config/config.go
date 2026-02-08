package config

import (
	"os"

	"github.com/joho/godotenv"
)

// Config holds all configuration for the auth service
type Config struct {
	ClerkSecretKey     string
	ClerkWebhookSecret string
	DatabaseURL        string
	Port               string
}

// Load reads configuration from environment variables
func Load() (*Config, error) {
	// Try to load .env file from multiple possible paths
	envPaths := []string{
		".env",          // Current directory
		"../../.env",    // When running from cmd/server/
		"../../../.env", // When running from deeper paths
	}

	for _, path := range envPaths {
		if err := godotenv.Load(path); err == nil {
			break
		}
	}

	cfg := &Config{
		ClerkSecretKey:     getEnv("CLERK_SECRET_KEY", ""),
		ClerkWebhookSecret: getEnv("CLERK_WEBHOOK_SECRET", ""),
		DatabaseURL:        getEnv("DATABASE_URL", ""),
		Port:               getEnv("PORT", "8080"),
	}

	return cfg, nil
}

func getEnv(key, defaultValue string) string {
	if value := os.Getenv(key); value != "" {
		return value
	}
	return defaultValue
}
