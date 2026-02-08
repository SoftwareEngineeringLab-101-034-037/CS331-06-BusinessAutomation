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
