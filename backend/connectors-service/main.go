package main

import (
	"log"
	"net/http"
	"os"

	"github.com/CS331-BusinessAutomation/connectors-service/api"
	"github.com/CS331-BusinessAutomation/connectors-service/pkg/connectors"
	"github.com/CS331-BusinessAutomation/connectors-service/pkg/connectors/gmail"
)

func main() {
	// Initialize Registry
	registry := connectors.NewRegistry()

	// Register Connectors
	gmailConnector := gmail.NewGmailConnector()
	registry.Register(gmailConnector)

	// Initialize API Handler
	handler := api.NewHandler(registry)

	// Setup Router
	http.HandleFunc("/trigger", handler.TriggerConnector)

	// Start Server
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	log.Printf("Connectors Service running on port %s", port)
	log.Printf("Available connectors: %s", gmailConnector.Name())

	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
