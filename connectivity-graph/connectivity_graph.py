#===============================================================================

import ipycytoscape
import networkx as nx

#===============================================================================

from mapknowledge import KnowledgeStore

store = KnowledgeStore('.')

def label(term):
    if term is not None:
        label = store.label(term)
        return f'{term}: {label}' if label is not None else term
    return ''

def node_id(node):
    names = [label(node[0])]
    for term in node[1]:
        names.append(label(term))
    return '\n'.join(names)

def connectivity_graph(neuron_population_id):
    knowledge = store.entity_knowledge(neuron_population_id)
    G = nx.Graph()
    for n, pair in enumerate(knowledge.get('connectivity', [])):
        nodes = (node_id(pair[0]),
                 node_id(pair[1]))
        if (nodes[0] != nodes[1]):
            G.add_edge(*nodes, directed=True, id=n)
            n += 1
    return G

#===============================================================================

style = [
       { 'selector': 'node',
         'style': {
             'label': 'data(id)',
             'background-color': '#80F0F0',
             'text-valign': 'center',
             'text-wrap': 'wrap',
             'text-max-width': '80px',
             'font-size': '10px'
         }
       },
       { 'selector': 'edge',
         'style': {
             'width': 2,
             'line-color': '#9dbaea',
         }
       }
]

def show_graph(neuron_population_id):
    G = connectivity_graph(neuron_population_id)
    g = ipycytoscape.CytoscapeWidget()
    g.graph.add_graph_from_networkx(G, directed=True)
    g.set_style(style)
    display(g)

#===============================================================================
