package models

import (
	"time"
)

// OrganizationSettings stores additional settings for an organization
type OrganizationSettings struct {
	ID             string    `gorm:"primaryKey;type:uuid;default:gen_random_uuid()" json:"id"`
	OrganizationID string    `gorm:"uniqueIndex;not null" json:"organization_id"` // FK to organizations table
	Domain         string    `json:"domain"`
	Industry       string    `json:"industry"`
	Size           string    `json:"size"`
	Country        string    `json:"country"`
	UseCase        string    `json:"use_case"`
	CreatedAt      time.Time `json:"created_at"`
	UpdatedAt      time.Time `json:"updated_at"`

	// Relationships
	Organization Organization `gorm:"foreignKey:OrganizationID" json:"organization,omitempty"`
}

// TableName specifies the table name for GORM
func (OrganizationSettings) TableName() string {
	return "organization_settings"
}
