package middleware

import (
	"log"
	"net/http"
	"strings"

	"github.com/clerk/clerk-sdk-go/v2/jwt"
	"github.com/gin-gonic/gin"
)

const (
	// UserIDKey is the context key for user ID
	UserIDKey = "userId"
	// OrgIDKey is the context key for organization ID
	OrgIDKey = "orgId"
	// SessionKey is the context key for session claims
	SessionKey = "session"
)

// AuthMiddleware validates Clerk JWTs and injects user context
type AuthMiddleware struct {
	secretKey string
}

// NewAuthMiddleware creates a new auth middleware
func NewAuthMiddleware(secretKey string) *AuthMiddleware {
	return &AuthMiddleware{secretKey: secretKey}
}

// Authenticate returns a Gin middleware that validates JWT tokens
func (m *AuthMiddleware) Authenticate() gin.HandlerFunc {
	return func(c *gin.Context) {
		// Extract token from Authorization header
		authHeader := c.GetHeader("Authorization")
		if authHeader == "" {
			c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{"error": "Missing authorization header"})
			return
		}

		// Remove "Bearer " prefix
		token := strings.TrimPrefix(authHeader, "Bearer ")
		if token == authHeader {
			c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{"error": "Invalid authorization format"})
			return
		}

		// Verify the token using Clerk JWT
		claims, err := jwt.Verify(c.Request.Context(), &jwt.VerifyParams{
			Token: token,
		})
		if err != nil {
			log.Printf(" JWT verification failed: %v", err)
			c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{"error": "Invalid or expired token"})
			return
		}

		// Extract user ID from claims (Subject is the user ID)
		userID := claims.Subject

		// Get organization ID from claims if present
		orgID := ""
		if claims.ActiveOrganizationID != "" {
			orgID = claims.ActiveOrganizationID
		}

		// Set values in Gin context
		c.Set(UserIDKey, userID)
		c.Set(OrgIDKey, orgID)
		c.Set(SessionKey, claims)

		c.Next()
	}
}

// GetUserID extracts user ID from Gin context
func GetUserID(c *gin.Context) string {
	if userID, exists := c.Get(UserIDKey); exists {
		return userID.(string)
	}
	return ""
}

// GetOrgID extracts organization ID from Gin context
func GetOrgID(c *gin.Context) string {
	if orgID, exists := c.Get(OrgIDKey); exists {
		return orgID.(string)
	}
	return ""
}

// OptionalAuth returns a Gin middleware that allows unauthenticated requests
func (m *AuthMiddleware) OptionalAuth() gin.HandlerFunc {
	return func(c *gin.Context) {
		authHeader := c.GetHeader("Authorization")
		if authHeader == "" {
			c.Next()
			return
		}

		token := strings.TrimPrefix(authHeader, "Bearer ")
		claims, err := jwt.Verify(c.Request.Context(), &jwt.VerifyParams{
			Token: token,
		})
		if err != nil {
			// Invalid token, but continue without auth
			c.Next()
			return
		}

		userID := claims.Subject
		orgID := ""
		if claims.ActiveOrganizationID != "" {
			orgID = claims.ActiveOrganizationID
		}

		c.Set(UserIDKey, userID)
		c.Set(OrgIDKey, orgID)
		c.Set(SessionKey, claims)

		c.Next()
	}
}
