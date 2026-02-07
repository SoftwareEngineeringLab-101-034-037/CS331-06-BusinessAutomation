from graphviz import Digraph

# Change format to 'svg' for svg
OUT_FORMAT = 'png'

dfd = Digraph('Level0_DFD_Pro', format=OUT_FORMAT)

# ===================== GRAPH SETTINGS =====================
dfd.attr(
    rankdir='TB',
    size='32,24!',
    dpi='300',
    bgcolor='#FFFFFF',
    pad='2.0',
    nodesep='2.5',
    ranksep='3.0',
    splines='ortho'
)


dfd.attr('edge', arrowsize='1.2', fontname='Arial', fontsize='14', penwidth='2', color='#333333', labeldistance='0', labelangle='0')

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
    fixedsize='true', margin='0.5'
)


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

# ===================== DATA FLOWS (runtime / events) =====================
dfd.edge('org_admin', 'system', taillabel='Org config / User management', labeldistance='11', labelangle='20')
dfd.edge('system', 'org_admin', headlabel='Confirmation / Status', labeldistance='7', labelangle='-90')

dfd.edge('admin', 'system', headlabel='Workflow / Task / Onboarding management', labeldistance='20', labelangle='-5')
dfd.edge('system', 'admin', taillabel='Confirmation / Status', labeldistance='20', labelangle='-5')

dfd.edge('analyst', 'system', taillabel='Report Query', labeldistance='8', labelangle='-15')
dfd.edge('system', 'analyst', taillabel='Metrics / Insights', labeldistance='9', labelangle='-15')

dfd.edge('employee', 'system', headlabel='Submit Request / Task Update', labeldistance='13', labelangle='-50')
dfd.edge('system', 'employee', headlabel='Tasks / Notifications / Status', labeldistance='9', labelangle='-14')

dfd.edge('new_employee', 'system', headlabel='Join Request / Data', labeldistance='20', labelangle='5')
dfd.edge('system', 'new_employee', taillabel='Invite / Onboarding Tasks', labeldistance='20', labelangle='5')

dfd.edge('system', 'external_services', headlabel='Trigger Actions (email/sms/calendar)', labeldistance='7', labelangle='-30')
dfd.edge('external_services', 'system', taillabel='Delivery Status', labeldistance='5', labelangle='15')

# Identity Provider - explicit one-way flows each direction (clear arrowheads)
dfd.edge('system', 'idp', headlabel='Auth Request (validate)', labeldistance='8', labelangle='15')
dfd.edge('idp', 'system', headlabel='Auth Token / User Identity', labeldistance='9', labelangle='15')

# Authentication Service - handles session management and access control
dfd.edge('system', 'auth_service', taillabel='Session Token / Access Decision', labeldistance='20', labelangle='45')
dfd.edge('auth_service', 'system', taillabel='Session / Access Request', labeldistance='8', labelangle='30')

# ===================== LAYOUT =====================
# North (Top)
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('admin')
    s.node('org_admin')
    s.node('analyst')
    s.node('employee')
    s.node('new_employee')

# Invisible edges to force left-to-right order on top row
dfd.edge('admin', 'org_admin', style='invis')
dfd.edge('org_admin', 'analyst', style='invis')
dfd.edge('analyst', 'employee', style='invis')
dfd.edge('employee', 'new_employee', style='invis')

# Middle layer with central process (alone)
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('system')


# ===================== TITLE =====================
dfd.attr(
    label='\\nLevel 0 Data Flow Diagram — Business Process Automation Platform\\n\n\n',
    labelloc='t',
    fontsize='20',
    fontname='Arial Bold'
)

# ===================== RENDER =====================
# Renders to Level0_DFD_Pro.svg (or .png if OUT_FORMAT='png')
outpath = dfd.render('Level0_DFD_Pro', cleanup=True)
print(f"✓ Diagram generated: {outpath}")
