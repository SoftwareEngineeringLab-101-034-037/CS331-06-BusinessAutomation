package model

import (
	"time"
)

// Workflow represents a workflow definition.
type Workflow struct {
	ID    string `json:"id"`
	Name  string `json:"name"`
	Steps []Step `json:"steps"`
}

// Step represents a single step in a workflow.
type Step struct {
	Name      string                 `json:"name"`
	Type      string                 `json:"type"`      // e.g., "connector"
	Reference string                 `json:"reference"` // e.g., "gmail"
	Payload   map[string]interface{} `json:"payload"`   // Args for the step
}

// Instance represents a running instance of a workflow.
type Instance struct {
	ID          string    `json:"id"`
	WorkflowID  string    `json:"workflow_id"`
	Status      string    `json:"status"` // "Running", "Completed", "Failed"
	CurrentStep int       `json:"current_step"`
	Logs        []string  `json:"logs"`
	CreatedAt   time.Time `json:"created_at"`
	UpdatedAt   time.Time `json:"updated_at"`
}
