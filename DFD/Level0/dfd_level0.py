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
dfd.node('analyst', 'Analyst', **user_style)

dfd.node('employee', 'Employee', **user_style)
dfd.node('manager', 'Manager', **user_style)
dfd.node('new_employee', 'New Employee', **user_style)

dfd.node('external_services', 'External Services\n(Email / SMS / Calendar)', **system_style)
dfd.node('idp', 'Identity Provider\n(IdP)', **system_style)

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

dfd.edge('analyst', 'system', xlabel='Report Query')
dfd.edge('system', 'analyst', xlabel='Metrics / Insights')

dfd.edge('employee', 'system', xlabel='Submit Request / Task Update')
dfd.edge('system', 'employee', xlabel='Tasks / Notifications / Status')

dfd.edge('manager', 'system', xlabel='Pending Tasks / Escalations')
dfd.edge('system', 'manager', xlabel='Approve / Reject')

dfd.edge('new_employee', 'system', xlabel='Join Request / Data')
dfd.edge('system', 'new_employee', xlabel='Invite / Onboarding Tasks')

dfd.edge('system', 'external_services', xlabel='Trigger Actions (email/sms/calendar)')
dfd.edge('external_services', 'system', xlabel='Delivery Status')

# Identity Provider - explicit one-way flows each direction (clear arrowheads)
dfd.edge('system', 'idp', xlabel='Auth Request (validate)')
dfd.edge('idp', 'system', xlabel='Auth Token / User Identity')