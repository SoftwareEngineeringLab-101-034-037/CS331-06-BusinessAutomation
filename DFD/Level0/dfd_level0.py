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

