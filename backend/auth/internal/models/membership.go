package models

import (
	"time"
)

// OrganizationMembership tracks user membership in organizations
type OrganizationMembership struct {
	ID             string    `gorm:"primaryKey" json:"id"` // Clerk membership ID
	UserID         string    `gorm:"not null;index" json:"user_id"`
	OrganizationID string    `gorm:"not null;index" json:"organization_id"`
	ClerkRole      string    `gorm:"not null" json:"clerk_role"` // admin, member
	LocalRoleID    *string   `json:"local_role_id"`              // FK to local Role
	JoinedAt       time.Time `json:"joined_at"`
	CreatedAt      time.Time `json:"created_at"`
	UpdatedAt      time.Time `json:"updated_at"`

	// Relationships
	User         User         `gorm:"foreignKey:UserID" json:"user,omitempty"`
	Organization Organization `gorm:"foreignKey:OrganizationID" json:"organization,omitempty"`
	LocalRole    *Role        `gorm:"foreignKey:LocalRoleID" json:"local_role,omitempty"`
}

// TableName specifies the table name for GORM
func (OrganizationMembership) TableName() string {
	return "organization_memberships"
}

// IsOrgAdmin checks if the membership has admin role in Clerk
func (m *OrganizationMembership) IsOrgAdmin() bool {
	return m.ClerkRole == "org:admin" || m.ClerkRole == "admin"
}
