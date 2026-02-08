package handler

import (
	"io"
	"log"
	"net/http"
	"time"

	"encoding/json"

	"github.com/gin-gonic/gin"
	svix "github.com/svix/svix-webhooks/go"

	"github.com/CS331-06-BusinessAutomation/backend/auth/internal/database"
	"github.com/CS331-06-BusinessAutomation/backend/auth/internal/models"
)

// WebhookHandler handles Clerk webhook events
type WebhookHandler struct {
	webhookSecret string
}

// NewWebhookHandler creates a new webhook handler
func NewWebhookHandler(secret string) *WebhookHandler {
	return &WebhookHandler{webhookSecret: secret}
}

// ClerkWebhookEvent represents the structure of a Clerk webhook payload
type ClerkWebhookEvent struct {
	Type   string          `json:"type"`
	Data   json.RawMessage `json:"data"`
	Object string          `json:"object"`
}

// ClerkUser represents user data from Clerk webhook
type ClerkUser struct {
	ID             string `json:"id"`
	EmailAddresses []struct {
		EmailAddress string `json:"email_address"`
	} `json:"email_addresses"`
	FirstName    string `json:"first_name"`
	LastName     string `json:"last_name"`
	ImageURL     string `json:"image_url"`
	CreatedAt    int64  `json:"created_at"`
	UpdatedAt    int64  `json:"updated_at"`
	LastSignInAt *int64 `json:"last_sign_in_at"`
}

// ClerkOrganization represents organization data from Clerk webhook
type ClerkOrganization struct {
	ID        string `json:"id"`
	Name      string `json:"name"`
	Slug      string `json:"slug"`
	ImageURL  string `json:"image_url"`
	CreatedAt int64  `json:"created_at"`
	UpdatedAt int64  `json:"updated_at"`
}

// Handle processes incoming Clerk webhooks
func (h *WebhookHandler) Handle(c *gin.Context) {
	// Read the request body
	body, err := io.ReadAll(c.Request.Body)
	if err != nil {
		log.Printf("Error reading webhook body: %v", err)
		c.JSON(http.StatusBadRequest, gin.H{"error": "Error reading request body"})
		return
	}

	// Verify the webhook signature using Svix. We do this because anyone on the web can send a webhook request to our backendURL. clerk signs its webhooks with a secret signature here we verify the webhook is indeed from clerk.
	wh, err := svix.NewWebhook(h.webhookSecret)
	if err != nil {
		log.Printf("Error creating webhook verifier: %v", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal server error"})
		return
	}

	headers := http.Header{}
	headers.Set("svix-id", c.GetHeader("svix-id"))
	headers.Set("svix-timestamp", c.GetHeader("svix-timestamp"))
	headers.Set("svix-signature", c.GetHeader("svix-signature"))

	err = wh.Verify(body, headers)
	if err != nil {
		log.Printf("Invalid webhook signature: %v", err)
		c.JSON(http.StatusUnauthorized, gin.H{"error": "Invalid signature"})
		return
	}

	// Parse the webhook event
	var event ClerkWebhookEvent
	if err := json.Unmarshal(body, &event); err != nil {
		log.Printf("Error parsing webhook event: %v", err)
		c.JSON(http.StatusBadRequest, gin.H{"error": "Error parsing event"})
		return
	}

	log.Printf("Received Clerk webhook: %s", event.Type)

	// Route to appropriate handler
	switch event.Type {
	case "user.created":
		h.handleUserCreated(event.Data)
	case "user.updated":
		h.handleUserUpdated(event.Data)
	case "user.deleted":
		h.handleUserDeleted(event.Data)
	case "organization.created":
		h.handleOrganizationCreated(event.Data)
	case "organization.deleted":
		h.handleOrganizationDeleted(event.Data)
	default:
		log.Printf("Unhandled webhook event type: %s", event.Type)
	}

	c.JSON(http.StatusOK, gin.H{"received": true})
}

// This function handles the backend when clerk sends a webhook saying a new user is created
func (h *WebhookHandler) handleUserCreated(data json.RawMessage) {
	var clerkUser ClerkUser
	if err := json.Unmarshal(data, &clerkUser); err != nil {
		log.Printf("Error parsing user data: %v", err)
		return
	}

	email := ""
	if len(clerkUser.EmailAddresses) > 0 {
		email = clerkUser.EmailAddresses[0].EmailAddress
	}

	user := models.User{
		ID:        clerkUser.ID,
		Email:     email,
		FirstName: clerkUser.FirstName,
		LastName:  clerkUser.LastName,
		AvatarURL: clerkUser.ImageURL,
		IsActive:  true,
		CreatedAt: time.UnixMilli(clerkUser.CreatedAt),
		UpdatedAt: time.UnixMilli(clerkUser.UpdatedAt),
	}

	if err := database.DB.Create(&user).Error; err != nil {
		log.Printf("Error creating user: %v", err)
		return
	}

	log.Printf("User created: %s (%s)", user.ID, user.Email)
}

// This function handles the backend when clerk sends a webhook saying a user is updated
func (h *WebhookHandler) handleUserUpdated(data json.RawMessage) {
	var clerkUser ClerkUser
	if err := json.Unmarshal(data, &clerkUser); err != nil {
		log.Printf("Error parsing user data: %v", err)
		return
	}

	email := ""
	if len(clerkUser.EmailAddresses) > 0 {
		email = clerkUser.EmailAddresses[0].EmailAddress
	}

	updates := map[string]interface{}{
		"email":      email,
		"first_name": clerkUser.FirstName,
		"last_name":  clerkUser.LastName,
		"avatar_url": clerkUser.ImageURL,
		"updated_at": time.UnixMilli(clerkUser.UpdatedAt),
	}

	if err := database.DB.Model(&models.User{}).Where("id = ?", clerkUser.ID).Updates(updates).Error; err != nil {
		log.Printf("Error updating user: %v", err)
		return
	}

	log.Printf("User updated: %s", clerkUser.ID)
}

// This function handles the backend when clerk sends a webhook saying a user is deleted
func (h *WebhookHandler) handleUserDeleted(data json.RawMessage) {
	var clerkUser struct {
		ID string `json:"id"`
	}
	if err := json.Unmarshal(data, &clerkUser); err != nil {
		log.Printf("Error parsing user data: %v", err)
		return
	}

	// Soft delete - set isActive to false
	if err := database.DB.Model(&models.User{}).Where("id = ?", clerkUser.ID).Update("is_active", false).Error; err != nil {
		log.Printf("Error deleting user: %v", err)
		return
	}

	log.Printf("User deleted (soft): %s", clerkUser.ID)
}

// This function handles the backend when clerk sends a webhook saying a new organization is created
func (h *WebhookHandler) handleOrganizationCreated(data json.RawMessage) {
	var clerkOrg ClerkOrganization
	if err := json.Unmarshal(data, &clerkOrg); err != nil {
		log.Printf("Error parsing organization data: %v", err)
		return
	}

	// Get the creator's user ID from the webhook - this will be the org admin
	// Clerk sends created_by in the organization webhook
	var rawData map[string]interface{}
	if err := json.Unmarshal(data, &rawData); err != nil {
		log.Printf("Error parsing raw organization data: %v", err)
		return
	}

	orgAdminID := getString(rawData, "created_by")
	if orgAdminID == "" {
		log.Printf("No created_by user found for organization %s, will update later via membership", clerkOrg.ID)
	}

	org := models.Organization{
		ID:        clerkOrg.ID,
		Name:      clerkOrg.Name,
		Slug:      clerkOrg.Slug,
		ImageURL:  clerkOrg.ImageURL,
		IsActive:  true,
		CreatedAt: time.UnixMilli(clerkOrg.CreatedAt),
		UpdatedAt: time.UnixMilli(clerkOrg.UpdatedAt),
	}

	// Only set OrgAdminID if we have a valid user ID (may not exist in DB yet, that's OK with nullable FK)
	if orgAdminID != "" {
		org.OrgAdminID = &orgAdminID
	}

	if err := database.DB.Create(&org).Error; err != nil {
		log.Printf("Error creating organization: %v", err)
		return
	}

	// Create empty settings record - will be populated via API call from frontend
	settings := models.OrganizationSettings{
		OrganizationID: clerkOrg.ID,
		CreatedAt:      time.Now(),
		UpdatedAt:      time.Now(),
	}

	if err := database.DB.Create(&settings).Error; err != nil {
		log.Printf("Error creating organization settings: %v", err)
		// Don't fail the whole operation, settings can be created later
	}

	log.Printf(" Organization created: %s (%s) with admin: %s", org.ID, org.Name, orgAdminID)
}

func (h *WebhookHandler) handleOrganizationDeleted(data json.RawMessage) {
	var clerkOrg struct {
		ID string `json:"id"`
	}
	if err := json.Unmarshal(data, &clerkOrg); err != nil {
		log.Printf("Error parsing organization data: %v", err)
		return
	}

	// Soft delete
	if err := database.DB.Model(&models.Organization{}).Where("id = ?", clerkOrg.ID).Update("is_active", false).Error; err != nil {
		log.Printf("Error deleting organization: %v", err)
		return
	}

	log.Printf("Organization deleted (soft): %s", clerkOrg.ID)
}

// Helper functions
func getString(m map[string]interface{}, key string) string {
	if v, ok := m[key].(string); ok {
		return v
	}
	return ""
}
