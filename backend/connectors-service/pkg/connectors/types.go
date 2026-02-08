package connectors

// Connector defines the interface for external service connectors.
type Connector interface {
	// Name returns the unique name of the connector.
	Name() string
	// Trigger executes the connector logic with the given payload.
	Trigger(payload map[string]interface{}) error
}
