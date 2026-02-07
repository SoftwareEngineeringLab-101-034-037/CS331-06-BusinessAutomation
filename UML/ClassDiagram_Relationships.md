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

### 1.2 Department
**Purpose**: Represents a department within an organization.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| departmentId | String | private | Unique identifier |
| name | String | private | Department name |
| organizationId | String | private | Parent organization reference |
| parentDepartmentId | String | private | For hierarchical structure |
| createdAt | DateTime | private | Timestamp of creation |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(name, orgId) | public | Department | Creates a new department |
| update(name) | public | void | Updates department info |
| delete() | public | void | Deletes the department |
| getUsers() | public | List\<User\> | Returns users in department |
| getSubDepartments() | public | List\<Department\> | Gets child departments |

---

### 1.3 User
**Purpose**: Represents a user (employee, admin, etc.) in the system.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| userId | String | private | Unique identifier |
| email | String | private | User email address |
| passwordHash | String | private | Hashed password |
| firstName | String | private | First name |
| lastName | String | private | Last name |
| organizationId | String | private | Parent organization |
| departmentId | String | private | Associated department |
| isActive | Boolean | private | Whether user is active |
| createdAt | DateTime | private | Account creation timestamp |
| lastLoginAt | DateTime | private | Last login timestamp |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| register(email, password) | public | User | Registers a new user |
| authenticate(email, password) | public | AuthToken | Authenticates user |
| updateProfile(data) | public | void | Updates user profile |
| deactivate() | public | void | Deactivates user account |
| getRoles() | public | List\<Role\> | Gets assigned roles |
| assignRole(role) | public | void | Assigns a role to user |
| removeRole(role) | public | void | Removes a role from user |
| getTasks() | public | List\<Task\> | Gets user's assigned tasks |
| getRequests() | public | List\<Request\> | Gets user's submitted requests |

---


### 1.4 Role
**Purpose**: Defines a role with specific permissions for RBAC.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| roleId | String | private | Unique identifier |
| name | String | private | Role name (e.g., Manager, HR) |
| description | String | private | Role description |
| organizationId | String | private | Parent organization |
| permissions | List\<Permission\> | private | Associated permissions |
| isSystemRole | Boolean | private | Whether it's a system-defined role |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(name, desc, orgId) | public | Role | Creates a new role |
| update(name, desc) | public | void | Updates role info |
| delete() | public | void | Deletes the role |
| addPermission(perm) | public | void | Adds a permission |
| removePermission(perm) | public | void | Removes a permission |
| hasPermission(action) | public | Boolean | Checks if role has permission |
| getUsers() | public | List\<User\> | Gets users with this role |

---

### 1.5 Permission
**Purpose**: Represents a specific permission/capability.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| permissionId | String | private | Unique identifier |
| name | String | private | Permission name |
| resource | String | private | Resource being accessed |
| action | String | private | Action type (read, write, delete) |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(name, resource, action) | public | Permission | Creates permission |
| matches(resource, action) | public | Boolean | Checks if permission matches |

---
