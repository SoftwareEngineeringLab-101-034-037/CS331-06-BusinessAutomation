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