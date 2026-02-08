package connectors

import (
	"fmt"
	"sync"
)

// Registry manages the available connectors.
type Registry struct {
	connectors map[string]Connector
	mu         sync.RWMutex
}

// NewRegistry creates a new connector registry.
func NewRegistry() *Registry {
	return &Registry{
		connectors: make(map[string]Connector),
	}
}

// Register adds a connector to the registry.
func (r *Registry) Register(c Connector) {
	r.mu.Lock()
	defer r.mu.Unlock()
	r.connectors[c.Name()] = c
}

// Get retrieves a connector by name.
func (r *Registry) Get(name string) (Connector, error) {
	r.mu.RLock()
	defer r.mu.RUnlock()
	c, ok := r.connectors[name]
	if !ok {
		return nil, fmt.Errorf("connector '%s' not found", name)
	}
	return c, nil
}
