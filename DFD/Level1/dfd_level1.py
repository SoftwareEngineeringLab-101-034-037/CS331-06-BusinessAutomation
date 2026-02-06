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