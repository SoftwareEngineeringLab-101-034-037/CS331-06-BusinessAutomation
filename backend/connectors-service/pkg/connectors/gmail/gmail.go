package gmail

import (
	"fmt"
	"log"
	"net/smtp"
	"os"
)

// GmailConnector implements the Connector interface for sending emails via Gmail.
type GmailConnector struct {
	SmtpServer     string
	SmtpPort       string
	SenderEmail    string
	SenderPassword string
}

// NewGmailConnector creates a new instance of GmailConnector.
func NewGmailConnector() *GmailConnector {
	return &GmailConnector{
		SmtpServer:     "smtp.gmail.com",
		SmtpPort:       "587",
		SenderEmail:    os.Getenv("GMAIL_SENDER_EMAIL"),
		SenderPassword: os.Getenv("GMAIL_SENDER_PASSWORD"),
	}
}

// Name returns the name of the connector.
func (g *GmailConnector) Name() string {
	return "gmail"
}

// Trigger sends an email based on the payload.
// Expected payload keys: "to", "subject", "body"
func (g *GmailConnector) Trigger(payload map[string]interface{}) error {
	to, ok := payload["to"].(string)
	if !ok {
		return fmt.Errorf("missing or invalid 'to' field in payload")
	}
	subject, ok := payload["subject"].(string)
	if !ok {
		subject = "No Subject" // Default subject
	}
	body, ok := payload["body"].(string)
	if !ok {
		body = "" // Default empty body
	}

	// Basic check if credentials are set (mock mode if not)
	if g.SenderEmail == "" || g.SenderPassword == "" {
		log.Printf("[Dry Run] Triggering Gmail Connector:\nTo: %s\nSubject: %s\nBody: %s\n", to, subject, body)
		return nil
	}

	auth := smtp.PlainAuth("", g.SenderEmail, g.SenderPassword, g.SmtpServer)
	msg := []byte("From: " + g.SenderEmail + "\r\n" +
		"To: " + to + "\r\n" +
		"Subject: " + subject + "\r\n" +
		"\r\n" +
		body + "\r\n")

	addr := g.SmtpServer + ":" + g.SmtpPort
	err := smtp.SendMail(addr, auth, g.SenderEmail, []string{to}, msg)
	if err != nil {
		return fmt.Errorf("failed to send email: %w", err)
	}

	log.Printf("Email sent successfully to %s", to)
	return nil
}
