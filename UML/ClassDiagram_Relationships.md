# Class Diagram - Business Process Automation Platform

This document identifies the key classes, their attributes, methods, and visibility for the End-to-End Business Process Automation Platform.

---

## 1. Organization & User Management Classes

### 1.1 Organization
**Purpose**: Represents a tenant organization on the platform.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| organizationId | String | private | Unique identifier for the organization |
| name | String | private | Organization name |
| subdomain | String | private | Unique subdomain for multi-tenant access |
| createdAt | DateTime | private | Timestamp of creation |
| isActive | Boolean | private | Whether organization is active |
| settings | OrganizationSettings | private | Organization-level configuration |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(name, subdomain) | public | Organization | Creates a new organization |
| update(settings) | public | void | Updates organization settings |
| deactivate() | public | void | Deactivates the organization |
| getDepartments() | public | List\<Department\> | Returns all departments |
| addDepartment(dept) | public | void | Adds a new department |
| getUsers() | public | List\<User\> | Returns all users in organization |