# Auth Service

Authentication service for Business Automation Platform using **Go + Gin + Clerk** with Supabase PostgreSQL.

## Overview

- **Frontend Pages**: Landing page, `/join` (join organization), `/create-org` (create organization)
- **Authentication**: Handled by Clerk on the frontend; user/org data synced to database via webhooks
- **Database**: PostgreSQL via Supabase

## Getting Started

### Prerequisites

- Go 1.22+
- Node.js 18+
- Supabase account
- Clerk account

### Running the Application

**1. Start the Frontend:**

```bash
cd Frontend
npm run dev
```

**2. Start the Backend:**

```bash
cd backend/auth/cmd/server
go run main.go
```

This will:
- Load environment variables from `.env`
- Connect to Supabase PostgreSQL
- Run database migrations (create tables if not exist)
- Start the cleanup background job

## Project Structure

```
auth/
├── cmd/server/main.go       # Entry point
├── internal/
│   ├── cleanup/             # Background cleanup job
│   ├── config/              # Environment configuration
│   ├── database/            # DB connection & migrations
│   ├── handler/             # Webhook handlers
│   ├── middleware/          # Auth middleware
│   └── models/              # Database models
├── .env                     # Environment variables
└── README.md
```

## Database Models

| Model | Description |
|-------|-------------|
| `User` | User synced from Clerk |
| `Organization` | Organization synced from Clerk |
| `OrganizationSettings` | Additional org settings (industry, size, etc.) |

## Webhook Events Handled

| Event | Action |
|-------|--------|
| `user.created` | Create user in database |
| `user.updated` | Update user details |
| `user.deleted` | Soft delete (set `is_active = false`) |
| `organization.created` | Create organization + empty settings |
| `organization.deleted` | Soft delete organization |

## Cleanup Job

A background job runs every **5 minutes** to permanently delete soft-deleted records older than **30 days**.

This follows industry best practices for data retention and recovery.

## API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| GET | `/health` | No | Health check |
| POST | `/api/webhooks/clerk` | No (Svix verified) | Clerk webhook receiver |

## Environment Variables

Create a `.env` file in `backend/auth/`:

```env
CLERK_SECRET_KEY=sk_test_xxxxx
CLERK_WEBHOOK_SECRET=whsec_xxxxx
DATABASE_URL=postgresql://user:pass@host:port/db
PORT=8080
```

## Notes

Clerk webhooks only send core data (name, email, etc.). Extra fields like organization size, industry, and use case are **not** included in webhook payloads.

To store this additional data, you would need to:
1. Create a separate API endpoint called from the frontend after org creation
2. Or store in Clerk's `publicMetadata` and sync separately

This is outside the scope of the auth module.