package engine

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
	"time"

	"github.com/CS331-BusinessAutomation/workflow-engine/pkg/model"
	"github.com/google/uuid"
)

// Engine manages workflow execution.
type Engine struct {
	workflows map[string]*model.Workflow
	instances map[string]*model.Instance
	mu        sync.RWMutex
}

// NewEngine creates a new workflow engine.
func NewEngine() *Engine {
	return &Engine{
		workflows: make(map[string]*model.Workflow),
		instances: make(map[string]*model.Instance),
	}
}

// RegisterWorkflow adds a new workflow definition.
func (e *Engine) RegisterWorkflow(w *model.Workflow) string {
	e.mu.Lock()
	defer e.mu.Unlock()
	if w.ID == "" {
		w.ID = uuid.New().String()
	}
	e.workflows[w.ID] = w
	return w.ID
}

// StartWorkflow creates and starts a new instance.
func (e *Engine) StartWorkflow(workflowID string) (*model.Instance, error) {
	e.mu.RLock()
	workflow, ok := e.workflows[workflowID]
	e.mu.RUnlock()

	if !ok {
		return nil, fmt.Errorf("workflow not found: %s", workflowID)
	}

	instance := &model.Instance{
		ID:          uuid.New().String(),
		WorkflowID:  workflowID,
		Status:      "Running",
		CurrentStep: 0,
		CreatedAt:   time.Now(),
		UpdatedAt:   time.Now(),
	}

	e.mu.Lock()
	e.instances[instance.ID] = instance
	e.mu.Unlock()

	// Execute asynchronously
	go e.Execute(instance, workflow)

	return instance, nil
}

// Execute runs the workflow steps.
func (e *Engine) Execute(instance *model.Instance, workflow *model.Workflow) {
	log.Printf("Starting execution for instance %s (Workflow: %s)", instance.ID, workflow.Name)

	for i, step := range workflow.Steps {
		log.Printf("Executing Step %d: %s (%s)", i+1, step.Name, step.Type)

		var err error
		if step.Type == "connector" {
			err = e.triggerConnector(step.Reference, step.Payload)
		} else {
			log.Printf("Unknown step type: %s", step.Type)
		}

		if err != nil {
			log.Printf("Step failed: %v", err)
			e.updateStatus(instance.ID, "Failed", fmt.Sprintf("Step %s failed: %v", step.Name, err))
			return
		}

		e.updateStep(instance.ID, i+1)
	}

	e.updateStatus(instance.ID, "Completed", "Workflow completed successfully")
	log.Printf("Instance %s completed", instance.ID)
}

// triggerConnector calls the external connector service.
func (e *Engine) triggerConnector(connectorName string, payload map[string]interface{}) error {
	url := "http://localhost:8080/trigger"
	reqBody, _ := json.Marshal(map[string]interface{}{
		"connector": connectorName,
		"payload":   payload,
	})

	resp, err := http.Post(url, "application/json", bytes.NewBuffer(reqBody))
	if err != nil {
		return fmt.Errorf("failed to call connector service: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("connector service returned status: %s", resp.Status)
	}
	return nil
}

func (e *Engine) updateStatus(instanceID, status string, logMsg string) {
	e.mu.Lock()
	defer e.mu.Unlock()
	if instance, ok := e.instances[instanceID]; ok {
		instance.Status = status
		instance.UpdatedAt = time.Now()
		instance.Logs = append(instance.Logs, logMsg)
	}
}

func (e *Engine) updateStep(instanceID string, stepIndex int) {
	e.mu.Lock()
	defer e.mu.Unlock()
	if instance, ok := e.instances[instanceID]; ok {
		instance.CurrentStep = stepIndex
		instance.UpdatedAt = time.Now()
	}
}

// GetInstance retrieves an instance by ID.
func (e *Engine) GetInstance(id string) (*model.Instance, error) {
	e.mu.RLock()
	defer e.mu.RUnlock()
	if instance, ok := e.instances[id]; ok {
		return instance, nil
	}
	return nil, fmt.Errorf("instance not found")
}
