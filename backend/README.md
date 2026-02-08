# Backend Services

This directory contains the backend microservices for the Business Automation Platform.

## Services

### 1. Connectors Service (Port 8080)
**Purpose:** Handles external integrations (Gmail, Slack, etc.)

**Location:** `backend/connectors-service/`

**Run:**
```bash
cd backend/connectors-service
export GMAIL_SENDER_EMAIL="your-email@gmail.com"
export GMAIL_SENDER_PASSWORD="your-app-password"
go run main.go
```

### 2. Workflow Engine (Port 8081)
**Purpose:** Orchestrates business workflows and manages execution

**Location:** `backend/workflow-engine/`

**Run:**
```bash
cd backend/workflow-engine
go run main.go
```

## Architecture

```
Workflow Engine (8081) → Connectors Service (8080) → External Services (Gmail, etc.)
```

## Quick Start

1. Start both services in separate terminals
2. Create a workflow:
   ```bash
   curl -X POST http://localhost:8081/workflows -H "Content-Type: application/json" -d '{
     "name": "Test Workflow",
     "steps": [{
       "name": "Send Email",
       "type": "connector",
       "reference": "gmail",
       "payload": {
         "to": "recipient@example.com",
         "subject": "Test",
         "body": "Hello from Workflow Engine!"
       }
     }]
   }'
   ```
3. Execute the workflow using the returned ID
