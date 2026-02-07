from graphviz import Digraph

OUT_FORMAT = 'png'
OUTPUT_NAME = 'Level1_DFD'

dfd = Digraph('Level1_DFD', format=OUT_FORMAT)

# ===================== GLOBAL GRAPH SETTINGS =====================
dfd.attr(
    rankdir='TB',
    size='60,50!',
    dpi='300',
    bgcolor='#FFFFFF',
    pad='1.5',
    nodesep='2.0',
    ranksep='2.0',
    splines='ortho',
    forcelabels='true',
    outputorder='edgesfirst',
)
dfd.attr('edge',
    fontname='Arial',
    fontsize='14',
    penwidth='2',
    color='#424242',
)

# ===================== STYLES =====================
user_style = {
    'shape': 'box',
    'style': 'filled,rounded',
    'fillcolor': '#E3F2FD',
    'color': '#1976D2',
    'penwidth': '2.5',
    'fontname': 'Arial Bold',
    'fontsize': '15',
    'fontcolor': '#0D47A1',
}

ext_system_style = {
    'shape': 'box',
    'style': 'filled,rounded',
    'fillcolor': '#FCE4EC',
    'color': '#C2185B',
    'penwidth': '2.5',
    'fontname': 'Arial Bold',
    'fontsize': '15',
    'fontcolor': '#880E4F',
}

process_style = {
    'shape': 'circle',
    'style': 'filled',
    'fillcolor': '#FFF9C4',
    'color': '#F57F17',
    'penwidth': '3',
    'fontname': 'Arial Bold',
    'fontsize': '12',
    'fixedsize': 'true',
    'width': '1.8',
    'height': '1.8',
}

datastore_style = {
    'shape': 'box',
    'style': 'filled',
    'fillcolor': '#E8F5E9',
    'color': '#2E7D32',
    'penwidth': '2.5',
    'fontname': 'Arial Bold',
    'fontsize': '13',
    'fontcolor': '#1B5E20',
}

ds_edge = {'style': 'dashed', 'color': '#1B5E20', 'fontcolor': '#1B5E20'}
IP_COLOR = '#7B1FA2'
IP_FONT = '#4A148C'

# ===================== EXTERNAL ENTITIES =====================
dfd.node('org_admin',    'Organization\nAdmin',                      **user_style, width='2.4', height='0.9')
dfd.node('admin',        'Admin',                                    **user_style, width='2.0', height='0.9')
dfd.node('new_employee', 'New\nEmployee',                            **user_style, width='2.0', height='0.9')
dfd.node('employee',     'Employee',                                 **user_style, width='2.0', height='0.9')
dfd.node('analyst',      'Analyst',                                  **user_style, width='2.0', height='0.9')
dfd.node('idp',          'Identity Provider\n(IdP)',                  **ext_system_style, width='2.6', height='0.9')
dfd.node('auth_svc',     'Authentication\nService',                  **ext_system_style, width='2.6', height='0.9')
dfd.node('ext_svc',      'External Services\n(Email / SMS / Calendar)', **ext_system_style, width='3.6', height='0.9')

# ===================== PROCESSES =====================
processes = [
    ('p1', '1.0\nOrg & User\nMgmt'),
    ('p2', '2.0\nWorkflow\nDesign'),
    ('p3', '3.0\nWorkflow\nExecution'),
    ('p4', '4.0\nRequest\nLifecycle'),
    ('p5', '5.0\nTask\nOrchestration'),
    ('p6', '6.0\nRule\nEngine'),
    ('p7', '7.0\nNotification\nEngine'),
    ('p8', '8.0\nAudit &\nCompliance'),
    ('p9', '9.0\nAnalytics\n& Reporting'),
]

# ===================== DATA STORES =====================
datastores = [
    ('d1', 'D1 | User & Org Data'),
    ('d2', 'D2 | Workflow Defs'),
    ('d3', 'D3 | Requests & Tasks'),
    ('d4', 'D4 | Audit Logs'),
    ('d5', 'D5 | Business Rules'),
]

# ===================== VALIDATION BOOKKEEPING =====================
_inbound  = {pid: set() for pid, _ in processes}
_outbound = {pid: set() for pid, _ in processes}


def add_edge(a, b, **kwargs):
    label = kwargs.pop('label', None)
    if label is not None:
        dfd.edge(a, b, xlabel=label, **kwargs)
    else:
        dfd.edge(a, b, **kwargs)
    if a in _outbound:
        _outbound[a].add(b)
    if b in _inbound:
        _inbound[b].add(a)


# ===================== SYSTEM BOUNDARY CLUSTER =====================
with dfd.subgraph(name='cluster_system') as c:
    c.attr(
        label='System Boundary — Business Process Automation Platform',
        labelloc='t', fontsize='14', fontname='Arial Bold',
        color='#BDBDBD', style='rounded,filled', fillcolor='#FAFAFA', penwidth='2',
        margin='20',
    )
    for pid, plabel in processes:
        c.node(pid, plabel, **process_style)
    for dsid, dslabel in datastores:
        c.node(dsid, dslabel, **datastore_style, width='3.0', height='0.8')

    # Rank tiers inside cluster
    with c.subgraph() as r:
        r.attr(rank='same')
        r.node('p1'); r.node('p2')
    with c.subgraph() as r:
        r.attr(rank='same')
        r.node('p3'); r.node('p4')
    with c.subgraph() as r:
        r.attr(rank='same')
        r.node('p5'); r.node('p6')
    with c.subgraph() as r:
        r.attr(rank='same')
        r.node('p7'); r.node('p8'); r.node('p9')
    with c.subgraph() as r:
        r.attr(rank='same')
        r.node('d1'); r.node('d2'); r.node('d3'); r.node('d4'); r.node('d5')

    # Invisible ordering within tiers (skip pairs with real edges)
    c.edge('p1', 'p2', style='invis')
    c.edge('p3', 'p4', style='invis')
    c.edge('p7', 'p8', style='invis')
    c.edge('d1', 'd2', style='invis')
    c.edge('d2', 'd3', style='invis')
    c.edge('d3', 'd4', style='invis')
    c.edge('d4', 'd5', style='invis')

# ===================== EXTERNAL <-> PROCESS EDGES =====================
add_edge('org_admin', 'p1', label='User Config', weight='8')
add_edge('p1', 'org_admin', label='Confirmation', constraint='false')
add_edge('org_admin', 'p2', headlabel='Workflow Design', labeldistance='7', labelangle='12')

add_edge('admin', 'p2', headlabel='Workflow/Rule Config', weight='8', labeldistance='7', labelangle='12')
add_edge('p2', 'admin', taillabel='Published Status', constraint='false', labeldistance='7', labelangle='12')
add_edge('admin', 'p5', label='Manual Assign')

add_edge('new_employee', 'p1', label='Join Request', weight='8')
add_edge('p1', 'new_employee', label='Onboarding', constraint='false')

add_edge('employee', 'p4', taillabel='Submit Request', weight='8', labeldistance='7', labelangle='45')
add_edge('p4', 'employee', taillabel='Request Status', constraint='false', labeldistance='10', labelangle='-5')
add_edge('employee', 'p5', taillabel='Task Actions', labeldistance='14', labelangle='80')
add_edge('p5', 'employee', headlabel='Tasks', constraint='false', labeldistance='6', labelangle='-10')

add_edge('analyst', 'p9', label='Queries', weight='8')
add_edge('p9', 'analyst', label='Reports', constraint='false')

add_edge('p1', 'idp', label='Auth Request')
add_edge('idp', 'p1', label='Auth Token', constraint='false')

add_edge('p7', 'ext_svc', label='Notifications')
add_edge('ext_svc', 'p7', label='Delivery Status', constraint='false')

add_edge('p1', 'auth_svc', taillabel='Session Token / Access Decision', labeldistance='10', labelangle='-5')
add_edge('auth_svc', 'p1', headlabel='Session / Access Request', constraint='false', labeldistance='10', labelangle='-5')

# ===================== INTER-PROCESS FLOWS =====================
# Downward (constraining skeleton)
add_edge('p2', 'p3', label='Published Workflows',  color=IP_COLOR, fontcolor=IP_FONT, weight='5')
add_edge('p3', 'p5', label='Task Triggers',         color=IP_COLOR, fontcolor=IP_FONT, weight='5')
add_edge('p5', 'p7', label='Notify Trigger',        color=IP_COLOR, fontcolor=IP_FONT, weight='5')
add_edge('p3', 'p7', label='SLA Breaches',          color=IP_COLOR, fontcolor=IP_FONT)
add_edge('p1', 'p8', label='User Events',           color=IP_COLOR, fontcolor=IP_FONT)
add_edge('p3', 'p8', taillabel='Transitions',           color=IP_COLOR, fontcolor=IP_FONT, labeldistance='6', labelangle='-12')
add_edge('p5', 'p8', label='Task Actions',          color=IP_COLOR, fontcolor=IP_FONT)
add_edge('p8', 'p9', label='Log Data',              color=IP_COLOR, fontcolor=IP_FONT, weight='5')
add_edge('p3', 'p6', taillabel='Rule Evaluation',       color=IP_COLOR, fontcolor=IP_FONT, labeldistance='10', labelangle='-4')

# Lateral / backward (non-constraining)
add_edge('p4', 'p3', label='New Requests',      color=IP_COLOR, fontcolor=IP_FONT, constraint='false')
add_edge('p3', 'p4', label='Status Updates',    color=IP_COLOR, fontcolor=IP_FONT, constraint='false')
add_edge('p5', 'p3', label='Task Completion',   color=IP_COLOR, fontcolor=IP_FONT, constraint='false')
add_edge('p6', 'p3', label='Routing Decisions', color=IP_COLOR, fontcolor=IP_FONT, constraint='false')
add_edge('p5', 'p6', label='Assignment Rules',  color=IP_COLOR, fontcolor=IP_FONT, constraint='false')
add_edge('p6', 'p5', label='Assignments',       color=IP_COLOR, fontcolor=IP_FONT, constraint='false')

# ===================== DATA STORE ACCESS =====================
add_edge('p1', 'd1', taillabel='R/W', minlen='2', labeldistance='35', labelangle='2', **ds_edge)
add_edge('p7', 'd1', label='Read', **ds_edge)

add_edge('p2', 'd2', label='R/W', minlen='2', **ds_edge)
add_edge('p3', 'd2', taillabel='Read', labeldistance='35', labelangle='2', **ds_edge)

add_edge('p3', 'd3', label='R/W',  **ds_edge)
add_edge('p4', 'd3', label='R/W',  **ds_edge)
add_edge('p5', 'd3', label='R/W',  **ds_edge)
add_edge('p6', 'd3', label='Read', **ds_edge)
add_edge('p7', 'd3', label='Read', constraint='false', **ds_edge)
add_edge('p9', 'd3', label='Read', constraint='false', **ds_edge)

add_edge('p8', 'd4', label='Write', **ds_edge)
add_edge('p9', 'd4', taillabel='Read', labeldistance='7', labelangle='15',  **ds_edge)

add_edge('p2', 'd5', label='R/W',  **ds_edge)
add_edge('p6', 'd5', taillabel='Read', labeldistance='7', labelangle='15', **ds_edge)
add_edge('p3', 'd5', label='Read', constraint='false', **ds_edge)
add_edge('p5', 'd5', label='Read', constraint='false', **ds_edge)

# ===================== EXTERNAL ENTITY RANKS =====================
with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('new_employee'); s.node('idp'); s.node('auth_svc')
    s.node('org_admin'); s.node('admin'); s.node('employee')

with dfd.subgraph() as s:
    s.attr(rank='same')
    s.node('ext_svc'); s.node('analyst')

dfd.edge('new_employee', 'idp', style='invis')
dfd.edge('idp', 'auth_svc', style='invis')
dfd.edge('auth_svc', 'org_admin', style='invis')
dfd.edge('org_admin', 'admin', style='invis')
dfd.edge('admin', 'employee', style='invis')

dfd.edge('new_employee', 'ext_svc', style='invis')
dfd.edge('ext_svc', 'analyst', style='invis')

# ===================== LEGEND & TITLE =====================
legend_text = (
    "LEGEND\\n"
    "──────────────────\\n"
    "Blue Box = External User\\n"
    "Pink Box = External System\\n"
    "Yellow Circle = Internal Process\\n"
    "Green Box = Data Store\\n"
    "Green Dashed Line = Data Store Access\\n"
    "Purple Solid Line = Inter-process Flow\\n"
)
dfd.node('legend', legend_text,
    shape='box', style='filled,rounded',
    fillcolor='#F5F5F5', color='#9E9E9E', penwidth='2',
    fontsize='14', fontname='Arial',
)

dfd.attr(
    label='\\nLevel 1 Data Flow Diagram — Business Process Automation Platform\\n',
    labelloc='t',
    fontsize='20',
    fontname='Arial Bold',
)

# ===================== RENDER =====================
outpath = dfd.render(OUTPUT_NAME, cleanup=True)
print("✓ Diagram generated:", outpath)
