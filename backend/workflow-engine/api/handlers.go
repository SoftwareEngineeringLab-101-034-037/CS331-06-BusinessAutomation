package api

import (
	"encoding/json"
	"net/http"

	"github.com/CS331-BusinessAutomation/workflow-engine/pkg/engine"
	"github.com/CS331-BusinessAutomation/workflow-engine/pkg/model"
	"github.com/gorilla/mux"
)

// Handler holds dependencies for API handlers.
type Handler struct {
	Engine *engine.Engine
}

// NewHandler creates a new Handler.
func NewHandler(e *engine.Engine) *Handler {
	return &Handler{Engine: e}
}

// CreateWorkflow handles the creation of a new workflow definition.
func (h *Handler) CreateWorkflow(w http.ResponseWriter, r *http.Request) {
	var workflow model.Workflow
	if err := json.NewDecoder(r.Body).Decode(&workflow); err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	id := h.Engine.RegisterWorkflow(&workflow)
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(map[string]string{"id": id, "message": "Workflow created successfully"})
}

// StartWorkflowInstance handles the execution of a workflow.
func (h *Handler) StartWorkflowInstance(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	workflowID := vars["id"]

	instance, err := h.Engine.StartWorkflow(workflowID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusNotFound)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	json.NewEncoder(w).Encode(instance)
}

// GetInstance handles retrieving the status of a workflow instance.
func (h *Handler) GetInstance(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	instanceID := vars["id"]

	instance, err := h.Engine.GetInstance(instanceID)
	if err != nil {
		http.Error(w, err.Error(), http.StatusNotFound)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(instance)
}
