from graphviz import Digraph

# Change format to 'svg' for svg
OUT_FORMAT = 'png'

dfd = Digraph('Level0_DFD_Pro', format=OUT_FORMAT)

# ===================== GRAPH SETTINGS =====================
dfd.attr(
    rankdir='TB',
    size='28,20!',
    dpi='300',
    bgcolor='#FFFFFF',
    pad='1.2',
    nodesep='1.0',
    ranksep='1.6',
    splines='ortho'
)


dfd.attr('edge', arrowsize='1.2', fontname='Arial', fontsize='14', penwidth='2', color='#333333')

user_style = dict(
    shape='box', style='filled,rounded',
    fillcolor='#E3F2FD', color='#1976D2',
    penwidth='2.5', fontname='Arial Bold',
    fontsize='16'
)

system_style = dict(
    shape='box', style='filled,rounded',
    fillcolor='#FCE4EC', color='#C2185B',
    penwidth='2.5', fontname='Arial Bold',
    fontsize='16'
)

process_style = dict(
    shape='circle', style='filled',
    fillcolor='#FFF9C4', color='#F57F17',
    penwidth='4', fontname='Arial Bold',
    fontsize='18', width='5', height='5',
    fixedsize='true'
)

datastore_style = dict(
    shape='box', style='filled',
    fillcolor='#E8F5E9', color='#2E7D32',
    penwidth='2.5', fontname='Arial Bold',
    fontsize='16'
)

# darker, more visible purple for dashed datastore lines
DATASTORE_LINE_COLOR = '#6A1B9A'  # darker purple

# ===================== NODES =====================
dfd.node('org_admin', 'Organization Admin', **user_style)
dfd.node('admin', 'Admin', **user_style)
dfd.node('analyst', 'Analyst', **user_style)

dfd.node('employee', 'Employee', **user_style)
dfd.node('new_employee', 'New Employee', **user_style)

dfd.node('external_services', 'External Services\n(Email / SMS / Calendar)', **system_style)
dfd.node('idp', 'Identity Provider\n(IdP)', **system_style)
dfd.node('auth_service', 'Authentication\nService', **system_style)

dfd.node('system', '0\nBusiness Process\nAutomation Platform', **process_style)

dfd.node('ds_users', 'D1\nUser & Org Data', **datastore_style)
dfd.node('ds_workflows', 'D2\nWorkflow Definitions', **datastore_style)
dfd.node('ds_requests', 'D3\nRequests & Tasks', **datastore_style)
dfd.node('ds_audit', 'D4\nAudit Logs & Reports', **datastore_style)
dfd.node('ds_rules', 'D5\nBusiness Rules', **datastore_style)

# ===================== DATA FLOWS (runtime / events) =====================
# Use xlabel (xlabels) because orthogonal edges don't handle inline edge labels well
dfd.edge('org_admin', 'system', xlabel='Org config / User mgmt')
dfd.edge('system', 'org_admin', xlabel='Confirmation / Status')

dfd.edge('admin', 'system', xlabel='Workflow / Task / Onboarding mgmt')
dfd.edge('system', 'admin', xlabel='Confirmation / Status')

dfd.edge('analyst', 'system', xlabel='Report Query')
dfd.edge('system', 'analyst', xlabel='Metrics / Insights')

dfd.edge('employee', 'system', xlabel='Submit Request / Task Update')
dfd.edge('system', 'employee', xlabel='Tasks / Notifications / Status')

dfd.edge('new_employee', 'system', xlabel='Join Request / Data')
dfd.edge('system', 'new_employee', xlabel='Invite / Onboarding Tasks')

dfd.edge('system', 'external_services', xlabel='Trigger Actions (email/sms/calendar)')
dfd.edge('external_services', 'system', xlabel='Delivery Status')

# Identity Provider - explicit one-way flows each direction (clear arrowheads)
dfd.edge('system', 'idp', xlabel='Auth Request (validate)')
dfd.edge('idp', 'system', xlabel='Auth Token / User Identity')

# Authentication Service - handles session management and access control
dfd.edge('system', 'auth_service', xlabel='Session / Access Request')
dfd.edge('auth_service', 'system', xlabel='Session Token / Access Decision')

# D1: User & Org Data
# system -> datastore : Write
dfd.edge('system', 'ds_users', xlabel='Write: User & Org Data', style='dashed', color=DATASTORE_LINE_COLOR)
# datastore -> system : Read
dfd.edge('ds_users', 'system', xlabel='Read: User & Org Data', style='dashed', color=DATASTORE_LINE_COLOR)

# D2: Workflow Definitions (R/W)
dfd.edge('system', 'ds_workflows', xlabel='Write: Workflow Definitions', style='dashed', color=DATASTORE_LINE_COLOR)
dfd.edge('ds_workflows', 'system', xlabel='Read: Workflow Definitions', style='dashed', color=DATASTORE_LINE_COLOR)

# D3: Requests & Tasks (R/W)
dfd.edge('system', 'ds_requests', xlabel='Write: Requests & Tasks', style='dashed', color=DATASTORE_LINE_COLOR)
dfd.edge('ds_requests', 'system', xlabel='Read: Requests & Tasks', style='dashed', color=DATASTORE_LINE_COLOR)

# D4: Audit Logs (Write-only sink)
dfd.edge('system', 'ds_audit', xlabel='Write Logs (W)', style='dashed', color=DATASTORE_LINE_COLOR)
# Integrations may also log
dfd.edge('external_services', 'ds_audit', xlabel='Integration Logs', style='dashed', color=DATASTORE_LINE_COLOR)

# D5: Business Rules (Read-only)
dfd.edge('ds_rules', 'system', xlabel='Read: Business Rules', style='dashed', color=DATASTORE_LINE_COLOR)

# ===================== LAYOUT =====================
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('org_admin')
    s.node('admin')
    s.node('analyst')

with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('employee')
    s.node('new_employee')

with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('external_services')
    s.node('idp')
    s.node('auth_service')


with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('ds_users')
    s.node('ds_workflows')
    s.node('ds_requests')
    s.node('ds_audit')
    s.node('ds_rules')

# ===================== LEGEND  =====================
legend_text = (
    "Legend:\\n"
    "Solid line = runtime messages / events\\n"
    "Dashed line = datastore access (read/write)\\n"
    "Read = arrow toward system from datastore\\n"
    "Write = arrow from system toward datastore\\n"
    "Audit store = write-only sink"
)
# make legend larger and place near datastores by nudging rank
dfd.node('legend', legend_text, shape='plaintext', fontsize='12')
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('ds_audit')
    s.node('legend')


# ===================== TITLE =====================
dfd.attr(
    label='\\nLevel 0 Data Flow Diagram — Business Process Automation Platform\\n',
    labelloc='t',
    fontsize='20',
    fontname='Arial Bold'
)

# ===================== RENDER =====================
# Renders to Level0_DFD_Pro.svg (or .png if OUT_FORMAT='png')
outpath = dfd.render('Level0_DFD_Pro', cleanup=True)
print(f"✓ Diagram generated: {outpath}")