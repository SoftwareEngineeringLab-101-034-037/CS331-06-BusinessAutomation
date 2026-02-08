package api

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/CS331-BusinessAutomation/connectors-service/pkg/connectors"
)

// TriggerRequest represents the payload for triggering a connector.
type TriggerRequest struct {
	Connector string                 `json:"connector"`
	Payload   map[string]interface{} `json:"payload"`
}

// Handler holds dependencies for API handlers.
type Handler struct {
	Registry *connectors.Registry
}

// NewHandler creates a new Handler.
func NewHandler(r *connectors.Registry) *Handler {
	return &Handler{Registry: r}
}

// TriggerConnector handles the trigger request.
func (h *Handler) TriggerConnector(w http.ResponseWriter, r *http.Request) {
	log.Printf("Received trigger request from %s", r.RemoteAddr)

	if r.Method != http.MethodPost {
		log.Printf("Invalid method: %s", r.Method)
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var req TriggerRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		log.Printf("Failed to decode request body: %v", err)
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	log.Printf("Triggering connector: %s with payload: %+v", req.Connector, req.Payload)

	connector, err := h.Registry.Get(req.Connector)
	if err != nil {
		log.Printf("Connector not found: %v", err)
		http.Error(w, err.Error(), http.StatusNotFound)
		return
	}

	if err := connector.Trigger(req.Payload); err != nil {
		log.Printf("Error triggering connector: %v", err)
		http.Error(w, fmt.Sprintf("Error triggering connector: %v", err), http.StatusInternalServerError)
		return
	}

	log.Printf("Connector triggered successfully")
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"status": "success", "message": "Connector triggered successfully"})
}
