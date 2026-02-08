package main

import (
	"log"
	"net/http"
	"os"

	"github.com/CS331-BusinessAutomation/workflow-engine/api"
	"github.com/CS331-BusinessAutomation/workflow-engine/pkg/engine"
	"github.com/gorilla/mux"
)

func main() {
	// Initialize Engine
	eng := engine.NewEngine()

	// Initialize API Handler
	handler := api.NewHandler(eng)

	// Setup Router
	r := mux.NewRouter()
	r.HandleFunc("/workflows", handler.CreateWorkflow).Methods("POST")
	r.HandleFunc("/workflows/{id}/execute", handler.StartWorkflowInstance).Methods("POST")
	r.HandleFunc("/instances/{id}", handler.GetInstance).Methods("GET")

	// Start Server
	port := os.Getenv("PORT")
	if port == "" {
		port = "8081" // Default to 8081 to avoid conflict with connectors-service
	}

	log.Printf("Workflow Engine running on port %s", port)
	if err := http.ListenAndServe(":"+port, r); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
