package models

import (
	"time"

	"gorm.io/datatypes"
)

// Role represents a role with permissions for local RBAC
type Role struct {
	ID             string         `gorm:"primaryKey" json:"id"`
	Name           string         `gorm:"not null" json:"name"`
	Description    string         `json:"description"`
	OrganizationID string         `gorm:"index" json:"organization_id"` // Scoped to org
	Permissions    datatypes.JSON `gorm:"type:jsonb" json:"permissions"`
	IsSystemRole   bool           `gorm:"default:false" json:"is_system_role"`
	CreatedAt      time.Time      `json:"created_at"`
	UpdatedAt      time.Time      `json:"updated_at"`
}

// TableName specifies the table name for GORM
func (Role) TableName() string {
	return "roles"
}

// Permission represents a permission entry
type Permission struct {
	ID       string `gorm:"primaryKey" json:"id"`
	Name     string `gorm:"not null" json:"name"`
	Resource string `gorm:"not null" json:"resource"` // e.g., "workflow", "task"
	Action   string `gorm:"not null" json:"action"`   // e.g., "read", "write", "delete"
}

// TableName specifies the table name for GORM
func (Permission) TableName() string {
	return "permissions"
}

// HasPermission checks if role has a specific permission
func (r *Role) HasPermission(resource, action string) bool {
	// This is a simplified check - in production, parse the JSON properly
	// For now, return false as placeholder
	return false
}
