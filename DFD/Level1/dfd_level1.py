from graphviz import Digraph

# Create Level 1 DFD
dfd = Digraph('Level1_DFD', format='png')

# ===================== GRAPH SETTINGS =====================
dfd.attr(
    rankdir='TB',
    size='50,40!',           # BIGGER canvas
    dpi='300',
    bgcolor='#FFFFFF',
    pad='2.0',
    nodesep='1.8',           # MORE horizontal spacing
    ranksep='2.2',           # MORE vertical spacing
    splines='ortho'          # STRAIGHT EDGES - keeping as requested
)

# ===================== STYLING =====================

# External entities (users) - Blue boxes - BIGGER TEXT
user_style = {
    'shape': 'box',
    'style': 'filled,rounded',
    'fillcolor': '#E3F2FD',
    'color': '#1976D2',
    'penwidth': '3',
    'fontname': 'Arial Bold',
    'fontsize': '32',        # EVEN BIGGER
    'fontcolor': '#0D47A1'
}

# External systems - Pink boxes - BIGGER TEXT
ext_system_style = {
    'shape': 'box',
    'style': 'filled,rounded',
    'fillcolor': '#FCE4EC',
    'color': '#C2185B',
    'penwidth': '3',
    'fontname': 'Arial Bold',
    'fontsize': '32',        # EVEN BIGGER
    'fontcolor': '#880E4F'
}

# Subprocesses - Yellow circles - BIGGER TEXT
process_style = {
    'shape': 'circle',
    'style': 'filled',
    'fillcolor': '#FFF9C4',
    'color': '#F57F17',
    'penwidth': '4',
    'fontname': 'Arial Bold',
    'fontsize': '20',        # EVEN BIGGER
    'fontcolor': '#E65100'
}

# Data stores - Green boxes - BIGGER TEXT
datastore_style = {
    'shape': 'box',
    'style': 'filled',
    'fillcolor': '#E8F5E9',
    'color': '#2E7D32',
    'penwidth': '3',
    'fontname': 'Arial Bold',
    'fontsize': '32',        # EVEN BIGGER
    'fontcolor': '#1B5E20'
}

# Edge styling - BIGGER LABELS
dfd.attr('edge', fontname='Arial Bold', fontsize='18', penwidth='2.5', color='#424242', fontcolor='#212121')

# Colors
DATASTORE_LINE_COLOR = '#6A1B9A'
INTERPROCESS_COLOR = '#7B1FA2'
INTERPROCESS_FONT = '#4A148C'

# ===================== EXTERNAL ENTITIES =====================

# User entities - BIGGER nodes
dfd.node('org_admin', 'Organization\nAdmin', **user_style, width='3.2', height='1.6')
dfd.node('admin', 'Admin', **user_style, width='2.8', height='1.6')
dfd.node('employee', 'Employee', **user_style, width='2.8', height='1.6')
dfd.node('manager', 'Manager', **user_style, width='2.8', height='1.6')
dfd.node('new_employee', 'New\nEmployee', **user_style, width='2.8', height='1.6')
dfd.node('analyst', 'Analyst', **user_style, width='2.8', height='1.6')

# External Systems - BIGGER nodes
dfd.node('idp', 'Identity\nProvider', **ext_system_style, width='3.2', height='1.6')
dfd.node('external_services', 'External Services\n(Email/SMS/Zoom)', **ext_system_style, width='4.5', height='1.6')

# ===================== SUBPROCESSES (1.0 - 9.0) - BIGGER =====================

dfd.node('p1', '1.0\n──────────\nOrganization\n& User\nManagement', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p2', '2.0\n──────────\nWorkflow\nDesign &\nConfig', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p3', '3.0\n──────────\nWorkflow\nExecution\nEngine', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p4', '4.0\n──────────\nRequest\nLifecycle\nMgmt', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p5', '5.0\n──────────\nTask\nOrchestration\n& Assignment', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p6', '6.0\n──────────\nRule Engine\n& Policy\nEnforcement', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p7', '7.0\n──────────\nNotification\n& Escalation\nEngine', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p8', '8.0\n──────────\nAudit &\nCompliance\nMgmt', **process_style, width='2.8', height='2.8', fixedsize='true')
dfd.node('p9', '9.0\n──────────\nAnalytics\n& Reporting', **process_style, width='2.8', height='2.8', fixedsize='true')

# ===================== DATA STORES - BIGGER =====================

dfd.node('d1', 'D1 | User & Organization Data', **datastore_style, width='6.5', height='1.2')
dfd.node('d2', 'D2 | Workflow Definitions', **datastore_style, width='6.0', height='1.2')
dfd.node('d3', 'D3 | Requests & Tasks', **datastore_style, width='6.0', height='1.2')
dfd.node('d4', 'D4 | Audit Logs & Reports', **datastore_style, width='6.0', height='1.2')
dfd.node('d5', 'D5 | Business Rules', **datastore_style, width='5.5', height='1.2')

# ===================== DATA FLOWS =====================

# --- External Entity → Process Flows ---

# Organization Admin flows
dfd.edge('org_admin', 'p1', label='User Config')
dfd.edge('p1', 'org_admin', label='Confirmation')
dfd.edge('org_admin', 'p2', label='Workflow\nDesign')

# Admin flows
dfd.edge('admin', 'p2', label='Workflow/Rule\nConfig')
dfd.edge('admin', 'p5', label='Manual\nAssignment')

# New Employee flows
dfd.edge('new_employee', 'p1', label='Join Request')
dfd.edge('p1', 'new_employee', label='Onboarding')

# Employee flows
dfd.edge('employee', 'p4', label='Submit\nRequest')
dfd.edge('p4', 'employee', label='Request\nStatus')
dfd.edge('p5', 'employee', label='Tasks')
dfd.edge('employee', 'p5', label='Task\nActions')

# Manager flows
dfd.edge('p5', 'manager', label='Pending\nTasks')
dfd.edge('manager', 'p5', label='Approvals')

# Analyst flows
dfd.edge('analyst', 'p9', label='Queries')
dfd.edge('p9', 'analyst', label='Reports &\nInsights')

# Identity Provider flows
dfd.edge('p1', 'idp', label='Auth Request')
dfd.edge('idp', 'p1', label='Auth Token')

# External Services flows
dfd.edge('p7', 'external_services', label='Notifications')
dfd.edge('external_services', 'p7', label='Delivery\nStatus')

# --- Inter-Process Flows (Purple) ---

# Workflow Design → Execution
dfd.edge('p2', 'p3', label='Published\nWorkflows', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Request Lifecycle → Execution
dfd.edge('p4', 'p3', label='New\nRequests', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Execution ↔ Task Orchestration
dfd.edge('p3', 'p5', label='Task\nTriggers', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)
dfd.edge('p5', 'p3', label='Task\nCompletion', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Execution → Request Lifecycle
dfd.edge('p3', 'p4', label='Status\nUpdates', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Execution ↔ Rule Engine
dfd.edge('p3', 'p6', label='Rule\nEvaluation', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)
dfd.edge('p6', 'p3', label='Routing\nDecisions', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Task ↔ Rule Engine
dfd.edge('p5', 'p6', label='Assignment\nRules', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)
dfd.edge('p6', 'p5', label='Assignments', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Notification triggers
dfd.edge('p5', 'p7', label='Notify\nTrigger', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)
dfd.edge('p3', 'p7', label='SLA\nBreaches', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Audit logging
dfd.edge('p1', 'p8', label='User\nEvents', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)
dfd.edge('p3', 'p8', label='Transitions', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)
dfd.edge('p5', 'p8', label='Task\nActions', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# Analytics
dfd.edge('p8', 'p9', label='Log Data', color=INTERPROCESS_COLOR, fontcolor=INTERPROCESS_FONT)

# --- Data Store Flows (Dashed) ---
ds_style = {'style': 'dashed', 'color': DATASTORE_LINE_COLOR, 'fontcolor': '#1B5E20'}

# D1: User & Organization Data
dfd.edge('p1', 'd1', label='R/W', **ds_style)
dfd.edge('p7', 'd1', label='Read', **ds_style)

# D2: Workflow Definitions
dfd.edge('p2', 'd2', label='R/W', **ds_style)
dfd.edge('p3', 'd2', label='Read', **ds_style)

# D3: Requests & Tasks
dfd.edge('p3', 'd3', label='R/W', **ds_style)
dfd.edge('p4', 'd3', label='R/W', **ds_style)
dfd.edge('p5', 'd3', label='R/W', **ds_style)
dfd.edge('p6', 'd3', label='Read', **ds_style)
dfd.edge('p7', 'd3', label='Read', **ds_style)
dfd.edge('p9', 'd3', label='Read', **ds_style)

# D4: Audit Logs & Reports
dfd.edge('p8', 'd4', label='Write', **ds_style)
dfd.edge('p9', 'd4', label='Read', **ds_style)

# D5: Business Rules
dfd.edge('p2', 'd5', label='R/W', **ds_style)
dfd.edge('p3', 'd5', label='Read', **ds_style)
dfd.edge('p5', 'd5', label='Read', **ds_style)
dfd.edge('p6', 'd5', label='Read', **ds_style)



# ===================== LAYOUT GROUPING =====================

# Users left column
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('org_admin')
    s.node('new_employee')

with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('employee')
    s.node('manager')
    s.node('analyst')

# External systems right column
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('external_services')
    s.node('idp')

# Process row 1
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('p1')
    s.node('p2')

# Process row 2 (core)
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('p3')
    s.node('p4')
    s.node('p5')
    s.node('p6')

# Process row 3
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('p7')
    s.node('p8')
    s.node('p9')

# Data stores at bottom
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('d1')
    s.node('d2')
    s.node('d3')
    s.node('d4')
    s.node('d5')

# ===================== LEGEND =====================
legend_text = (
    "LEGEND\\n"
    "═════════════════════════════════\\n"
    "Blue Box = User (External Entity)\\n"
    "Pink Box = External System\\n"
    "Yellow Circle = Subprocess\\n"
    "Green Box = Data Store\\n"
    "═════════════════════════════════\\n"
    "Solid Line = Data Flow\\n"
    "Purple Line = Inter-Process Flow\\n"
    "Dashed Line = Data Store Access\\n"
)
dfd.node('legend', legend_text, shape='plaintext', fontsize='18', fontname='Arial Bold')

with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('d5')
    s.node('legend')