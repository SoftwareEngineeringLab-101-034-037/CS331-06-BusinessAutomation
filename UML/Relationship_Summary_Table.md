# UML Class Diagram - Relationship Summary Table
## Business Process Automation Platform

---

## COMPLETE RELATIONSHIP REFERENCE TABLE

| # | From Class | Relationship Type | To Class | Cardinality | Description |
|---|-----------|------------------|----------|-------------|-------------|
| **COMPOSITION RELATIONSHIPS** |
| 1 | Organization | Composition (◆) | Department | 1 to * | Organization owns departments |
| 2 | Workflow | Composition (◆) | WorkflowStep | 1 to * | Workflow contains steps |
| 3 | WorkflowStep | Composition (◆) | Transition | 1 to * | Step defines transitions |
| 4 | WorkflowStep | Composition (◆) | StepAction | 1 to * | Step provides actions |
| 5 | Request | Composition (◆) | Comment | 1 to * | Request contains comments |
| 6 | Request | Composition (◆) | Attachment | 1 to * | Request contains attachments |
| 7 | Request | Composition (◆) | TimelineEntry | 1 to * | Request tracks timeline |
| 8 | WorkflowInstance | Composition (◆) | ExecutionContext | 1 to 1 | Instance has context |
| **AGGREGATION RELATIONSHIPS** |
| 9 | Organization | Aggregation (◇) | User | 1 to * | Organization employs users |
| 10 | Department | Aggregation (◇) | User | 1 to * | Department contains users |
| 11 | Role | Aggregation (◇) | Permission | 1 to * | Role includes permissions |
| 12 | Policy | Aggregation (◇) | Rule | * to * | Policy enforces rules |
| 13 | TaskQueue | Aggregation (◇) | Task | 1 to * | Queue manages tasks |
| 14 | RuleEngine | Aggregation (◇) | Rule | 1 to * | Engine uses rules |
| 15 | EscalationEngine | Aggregation (◇) | EscalationPolicy | 1 to * | Engine applies policies |
| **ASSOCIATION RELATIONSHIPS** |
| 16 | User | Association (→) | Role | * to * | User has roles |
| 17 | User | Association (→) | Session | 1 to * | User creates sessions |
| 18 | User | Association (→) | Request | 1 to * | User submits requests |
| 19 | Task | Association (→) | User | * to 1 | Task assigned to user |
| 20 | Request | Association (→) | Workflow | * to 1 | Request instance of workflow |
| 21 | Request | Association (→) | WorkflowInstance | 1 to 1 | Request has instance |
| 22 | Request | Association (→) | Task | 1 to * | Request generates tasks |
| 23 | Task | Association (→) | WorkflowStep | * to 1 | Task based on step |
| 24 | Task | Association (→) | Role | * to 0..1 | Task assigned to role |
| 25 | WorkflowStep | Association (→) | Role | * to 1 | Step assigned to role |
| 26 | Transition | Association (→) | Rule | * to 0..1 | Transition evaluates rule |
| 27 | Notification | Association (→) | User | * to 1 | Notification sent to user |
| 28 | NotificationService | Association (→) | Notification | 1 to * | Service sends notifications |
| 29 | AnalyticsEngine | Association (→) | WorkflowMetrics | 1 to * | Engine generates metrics |
| 30 | SimulationEngine | Association (→) | Workflow | 1 to 1 | Engine simulates workflow |
| **DEPENDENCY RELATIONSHIPS** |
| 31 | NotificationService | Dependency (⇢) | Task | - | Service monitors tasks |
| 32 | EscalationEngine | Dependency (⇢) | Task | - | Engine monitors tasks |
| 33 | AnalyticsEngine | Dependency (⇢) | Workflow | - | Engine analyzes workflows |
| 34 | WebhookHandler | Dependency (⇢) | Request | - | Handler triggers requests |
| 35 | RuleEngine | Dependency (⇢) | Transition | - | Engine determines transitions |
| **INHERITANCE RELATIONSHIPS** |
| 36 | APIConnector | Inheritance (△) | ExternalServiceConnector | - | APIConnector extends base |
| **SELF-REFERENCE RELATIONSHIPS** |
| 37 | Department | Association (→) | Department | 0..1 to * | Department has parent |

---

## RELATIONSHIP TYPE LEGEND

| Symbol | Type | Meaning | Lifecycle |
|--------|------|---------|-----------|
| ◆ | Composition | Strong ownership | Child destroyed with parent |
| ◇ | Aggregation | Weak ownership | Child can exist independently |
| → | Association | General relationship | Independent lifecycles |
| ⇢ | Dependency | Uses relationship | Temporary connection |
| △ | Inheritance | Is-a relationship | Subclass extends parent |

---

## CARDINALITY NOTATION

| Notation | Meaning |
|----------|---------|
| 1 | Exactly one |
| 0..1 | Zero or one (optional) |
| * | Zero or more |
| 1..* | One or more |
| m..n | Between m and n |

---

## STATISTICS

- **Total Relationships**: 37
- **Composition**: 8
- **Aggregation**: 7
- **Association**: 15
- **Dependency**: 5
- **Inheritance**: 1
- **Self-Reference**: 1

---

## CLASS PARTICIPATION COUNT

| Class Name | Total Relationships | As Source | As Target |
|-----------|-------------------|-----------|-----------|
| User | 6 | 3 | 3 |
| Request | 8 | 5 | 3 |
| Task | 6 | 2 | 4 |
| Workflow | 3 | 1 | 2 |
| WorkflowStep | 6 | 4 | 2 |
| Organization | 2 | 2 | 0 |
| Department | 3 | 2 | 1 |
| Role | 4 | 1 | 3 |
| Rule | 4 | 0 | 4 |
| Transition | 2 | 1 | 1 |
| Notification | 1 | 1 | 0 |
| NotificationService | 2 | 2 | 0 |
| EscalationEngine | 2 | 2 | 0 |
| AnalyticsEngine | 2 | 2 | 0 |
| Others | 1-2 each | - | - |

---

## MOST CONNECTED CLASSES

1. **Request** (8 relationships)
   - Central entity in workflow execution
   - Connects workflow design to execution

2. **Task** (6 relationships)
   - Core work unit
   - Connects users, roles, steps, and requests

3. **WorkflowStep** (6 relationships)
   - Defines workflow structure
   - Bridge between design and execution

4. **User** (6 relationships)
   - Central actor in system
   - Interacts with most functional areas

---

## RELATIONSHIP PATTERNS

### Hub Pattern
- **Request**: Central hub connecting workflow definition to execution
- **User**: Central hub connecting authentication, authorization, and work

### Hierarchical Pattern
- **Organization → Department → User**: Organizational structure
- **Workflow → WorkflowStep → Transition**: Workflow structure

### Many-to-Many Pattern
- **User ↔ Role**: Flexible RBAC
- **Policy ↔ Rule**: Flexible policy management

### Monitoring Pattern
- **Services → Tasks/Workflows**: Monitoring and alerting through dependencies

---

## ASSUMPTIONS AND CONSTRAINTS

1. **Every Department must belong to exactly one Organization** (mandatory parent)
2. **Users can exist without roles** (0..* allows new users without role assignment)
3. **Workflows must have at least one step** (1..* ensures validity)
4. **Tasks can be assigned to either User OR Role** (0..1 allows unassigned or role-based)
5. **Transitions can be unconditional** (0..1 Rule allows simple sequential flow)
6. **Departments can form hierarchies** (self-reference for organizational trees)
7. **Requests always instantiate exactly one Workflow** (1 to 1 for traceability)
8. **Every Request has exactly one WorkflowInstance** (1 to 1 for execution tracking)

---

## DESIGN RATIONALE SUMMARY

### Why Composition for Workflow Components?
- Workflow definitions are structural
- Steps, Transitions, Actions have no meaning outside their workflow
- Deletion should cascade to maintain consistency

### Why Aggregation for Users?
- Users can be transferred between departments
- Users might exist temporarily during onboarding
- Organizational flexibility requires looser coupling

### Why Association for Runtime Entities?
- Requests, Tasks, Sessions have independent lifecycles
- Runtime relationships are dynamic
- Decoupling allows for flexibility in execution

### Why Many-to-Many for RBAC?
- Modern applications require users with multiple roles
- Roles should be reusable across users
- Separation of concerns between user identity and authorization

---

This table provides a complete reference for all 37 relationships in the Business Process Automation Platform UML class diagram.