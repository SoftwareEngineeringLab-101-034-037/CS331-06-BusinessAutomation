package database

import (
	"log"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"

	"github.com/CS331-06-BusinessAutomation/backend/auth/internal/models"
)

var DB *gorm.DB

// Connect establishes connection to Supabase PostgreSQL
func Connect(databaseURL string) error {
	var err error

	DB, err = gorm.Open(postgres.Open(databaseURL), &gorm.Config{
		Logger: logger.Default.LogMode(logger.Warn), // Only log warnings and errors
	})
	if err != nil {
		return err
	}

	log.Println("Connected to Supabase PostgreSQL")
	return nil
}

// Migrate runs database migrations
func Migrate() error {
	err := DB.AutoMigrate(
		&models.User{},
		&models.Organization{},
		&models.OrganizationSettings{},
	)
	if err != nil {
		return err
	}

	log.Println("Database migrations completed")
	return nil
}
