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

### 1.6 Session
**Purpose**: Manages user authentication sessions.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| sessionId | String | private | Unique session identifier |
| userId | String | private | Associated user |
| token | String | private | JWT or session token |
| createdAt | DateTime | private | Session creation time |
| expiresAt | DateTime | private | Session expiration time |
| ipAddress | String | private | Client IP address |
| isValid | Boolean | private | Whether session is valid |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(userId) | public | Session | Creates new session |
| validate(token) | public | Boolean | Validates session token |
| refresh() | public | Session | Refreshes session |
| invalidate() | public | void | Invalidates/logs out session |
| isExpired() | public | Boolean | Checks if session expired |

---

## 2. Workflow Design & Configuration Classes

### 2.1 Workflow
**Purpose**: Represents a workflow definition/template.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| workflowId | String | private | Unique identifier |
| name | String | private | Workflow name |
| description | String | private | Workflow description |
| organizationId | String | private | Owning organization |
| version | Integer | private | Version number |
| status | WorkflowStatus | private | Draft, Published, Archived |
| inputSchema | JSONSchema | private | Input data validation schema |
| createdBy | String | private | Creator user ID |
| createdAt | DateTime | private | Creation timestamp |
| publishedAt | DateTime | private | Publication timestamp |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(name, desc, orgId) | public | Workflow | Creates new workflow |
| update(data) | public | void | Updates workflow definition |
| publish() | public | void | Publishes workflow |
| archive() | public | void | Archives workflow |
| clone() | public | Workflow | Clones workflow for new version |
| validate() | public | ValidationResult | Validates workflow structure |
| getSteps() | public | List\<WorkflowStep\> | Gets all workflow steps |
| addStep(step) | public | void | Adds a step |
| removeStep(stepId) | public | void | Removes a step |
| getStartStep() | public | WorkflowStep | Gets initial step |
| getVersionHistory() | public | List\<Workflow\> | Gets version history |


### 2.2 WorkflowStep
**Purpose**: Represents a single step in a workflow.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| stepId | String | private | Unique identifier |
| workflowId | String | private | Parent workflow |
| name | String | private | Step name |
| description | String | private | Step description |
| stepType | StepType | private | Approval, Action, Decision, Parallel |
| sequence | Integer | private | Order in workflow |
| assignedRoleId | String | private | Role responsible for step |
| slaHours | Integer | private | SLA duration in hours |
| isStartStep | Boolean | private | Whether it's the start step |
| isEndStep | Boolean | private | Whether it's an end step |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(workflowId, data) | public | WorkflowStep | Creates new step |
| update(data) | public | void | Updates step configuration |
| delete() | public | void | Deletes the step |
| getTransitions() | public | List\<Transition\> | Gets outgoing transitions |
| addTransition(trans) | public | void | Adds a transition |
| getActions() | public | List\<StepAction\> | Gets available actions |
| getAssignedRole() | public | Role | Gets assigned role |

---

### 2.3 Transition
**Purpose**: Defines transition between workflow steps.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| transitionId | String | private | Unique identifier |
| fromStepId | String | private | Source step |
| toStepId | String | private | Destination step |
| triggerAction | String | private | Action that triggers (approve, reject) |
| condition | Rule | private | Conditional routing rule |
| priority | Integer | private | Priority for rule evaluation |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(fromStep, toStep, action) | public | Transition | Creates transition |
| update(data) | public | void | Updates transition |
| delete() | public | void | Deletes transition |
| setCondition(rule) | public | void | Sets conditional rule |
| evaluate(context) | public | Boolean | Evaluates if transition is valid |

---

### 2.4 StepAction
**Purpose**: Defines actions available at a workflow step.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| actionId | String | private | Unique identifier |
| stepId | String | private | Parent step |
| name | String | private | Action name (Approve, Reject, etc.) |
| label | String | private | Display label |
| requiresComment | Boolean | private | If comment is mandatory |
| requiresAttachment | Boolean | private | If attachment is required |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| create(stepId, name) | public | StepAction | Creates new action |
| update(data) | public | void | Updates action config |
| delete() | public | void | Deletes action |

---

## 3. Workflow Execution Engine Classes

### 3.1 Request
**Purpose**: Represents a workflow instance/execution.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| requestId | String | private | Unique identifier |
| workflowId | String | private | Source workflow |
| requesterId | String | private | User who submitted request |
| currentStepId | String | private | Current active step |
| status | RequestStatus | private | Pending, InProgress, Completed, Cancelled |
| inputData | JSON | private | Request input data |
| createdAt | DateTime | private | Submission timestamp |
| completedAt | DateTime | private | Completion timestamp |
| priority | Priority | private | Request priority level |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| submit(workflowId, data) | public | Request | Submits new request |
| cancel(reason) | public | void | Cancels the request |
| reopen() | public | void | Reopens cancelled request |
| getStatus() | public | RequestStatus | Gets current status |
| getCurrentStep() | public | WorkflowStep | Gets current step |
| getTimeline() | public | List\<TimelineEntry\> | Gets execution timeline |
| getTasks() | public | List\<Task\> | Gets all generated tasks |
| addComment(comment) | public | void | Adds a comment |
| addAttachment(file) | public | void | Adds an attachment |
| getComments() | public | List\<Comment\> | Gets all comments |
| getAttachments() | public | List\<Attachment\> | Gets all attachments |

---

### 3.2 WorkflowInstance
**Purpose**: Manages the execution state of a workflow.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| instanceId | String | private | Unique identifier |
| requestId | String | private | Associated request |
| workflowId | String | private | Workflow definition |
| state | ExecutionState | private | Current execution state |
| context | ExecutionContext | private | Execution context data |
| startedAt | DateTime | private | Execution start time |
| isRunning | Boolean | private | Whether currently executing |
| parallelBranches | List\<Branch\> | private | Active parallel branches |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| start(requestId) | public | void | Starts workflow execution |
| pause() | public | void | Pauses execution |
| resume() | public | void | Resumes execution |
| transitionTo(stepId) | public | void | Moves to next step |
| executeStep(stepId) | public | void | Executes a step |
| handleEvent(event) | public | void | Processes workflow event |
| synchronizeBranches() | protected | void | Syncs parallel branches |
| evaluateConditions(step) | protected | Transition | Evaluates routing rules |
| getState() | public | ExecutionState | Gets current state |
| saveState() | protected | void | Persists state |
| loadState() | protected | void | Loads state from storage |

---

### 3.3 ExecutionContext
**Purpose**: Holds runtime context for workflow execution.

| Attribute | Type | Visibility | Description |
|-----------|------|------------|-------------|
| contextId | String | private | Unique identifier |
| instanceId | String | private | Parent workflow instance |
| variables | Map\<String,Object\> | private | Workflow variables |
| requestData | JSON | private | Original request data |
| stepHistory | List\<StepExecution\> | private | History of step executions |

| Method | Visibility | Return Type | Description |
|--------|------------|-------------|-------------|
| getVariable(key) | public | Object | Gets a variable value |
| setVariable(key, value) | public | void | Sets a variable |
| getRequestData() | public | JSON | Gets request data |
| addToHistory(stepExec) | public | void | Adds step to history |
| getHistory() | public | List\<StepExecution\> | Gets step history |

---