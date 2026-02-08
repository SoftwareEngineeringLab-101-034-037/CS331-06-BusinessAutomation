package models

import (
	"time"
)

// Organization represents an organization synced from Clerk
type Organization struct {
	ID         string    `gorm:"primaryKey" json:"id"` // Clerk organization ID
	Name       string    `gorm:"not null" json:"name"`
	Slug       string    `gorm:"uniqueIndex" json:"slug"` // URL friendly shortform for the org
	ImageURL   string    `json:"image_url"`
	OrgAdminID *string   `gorm:"index" json:"org_admin_id"` // FK to users table (nullable - set via membership webhook)
	IsActive   bool      `gorm:"default:true" json:"is_active"`
	CreatedAt  time.Time `json:"created_at"`
	UpdatedAt  time.Time `json:"updated_at"`

	// Relationships
	OrgAdmin    User                     `gorm:"foreignKey:OrgAdminID" json:"org_admin,omitempty"`
	Settings    *OrganizationSettings    `gorm:"foreignKey:OrganizationID" json:"settings,omitempty"`
	Memberships []OrganizationMembership `gorm:"foreignKey:OrganizationID" json:"memberships,omitempty"`
}

// TableName specifies the table name for GORM
func (Organization) TableName() string {
	return "organizations"
}
