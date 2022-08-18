#===============================================================================
#
#  Flatmap viewer and annotation tools
#
#  Copyright (c) 2020-2022  David Brooks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#===============================================================================

import ipycytoscape
import networkx as nx

#===============================================================================

from mapknowledge import KnowledgeStore
from mapknowledge.scicrunch import SCICRUNCH_PRODUCTION, SCICRUNCH_STAGING

#===============================================================================

from all_graphs import graph_from_knowledge

LABEL_WIDTH = 16

def wrap_text(text, max_width=LABEL_WIDTH):
    words = text.strip().split()
    s = 0
    while True:
        l = 0
        e = s
        while e < len(words) and l < max_width:
            l += len(words[e])
            e += 1
        if l < max_width:
            yield ' '.join(words[s:e])
            return
        else:
            if e > (s + 1):
                e -= 1
            yield ' '.join(words[s:e])
            s = e

class ConnectivityKnowledge(KnowledgeStore):
    def __init__(self, store_directory=None, clean_connectivity=False,
                 scicrunch_release=SCICRUNCH_PRODUCTION, scicrunch_key=None):
        super().__init__(store_directory=store_directory,
                         clean_connectivity=clean_connectivity,
                         scicrunch_release=scicrunch_release,
                         scicrunch_key=scicrunch_key)

    def formatted_label(self, term):
        if term is not None:
            label = self.label(term)
            return '\n'.join(wrap_text(f'{term}: {label}' if label is not None else term))
        return ''

    def node_id(self, node):
        names = [self.formatted_label(node[0])]
        for term in node[1]:
            names.append(self.formatted_label(term))
        return '\n'.join(names)

    def connectivity(self, neuron_population_id):
        knowledge = self.entity_knowledge(neuron_population_id)
        G = nx.Graph()
        for n, pair in enumerate(knowledge.get('connectivity', [])):
            nodes = (self.node_id(pair[0]),
                     self.node_id(pair[1]))
            if (nodes[0] != nodes[1]):
                G.add_edge(*nodes, directed=True, id=n)
                n += 1
        return G

#===============================================================================

STYLING = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(label)',
            'background-color': '#80F0F0',
            'text-valign': 'center',
            'text-wrap': 'wrap',
            'text-max-width': '80px',
            'font-size': '10px'
        }
    },
    {'selector': 'node[axon]',
     'style': {'background-color': 'green',},},
    {'selector': 'node[dendrite]',
     'style': {'background-color': 'red',},},
    {'selector': 'node[both-a-d]',
     'style': {'background-color': 'gray',},},
    {
        'selector': 'edge',
        'style': {
            'width': 2,
            'line-color': '#9dbaea',
        }
    }
]


def display_connectivity(graph):
    for nodes in nx.connected_components(graph):
        G = graph.subgraph(nodes)
        g = ipycytoscape.CytoscapeWidget()
        g.graph.add_graph_from_networkx(G, directed=True)
        g.set_style(STYLING)
        display(g)


def all_the_things(store, nid):
    wat = store.entity_knowledge(nid)
    graph = graph_from_knowledge(store, wat)
    nodesm = list(nx.connected_components(graph))
    for hrm in nodesm:
        G = graph.subgraph(hrm)
        G.nodes[list(G.nodes.keys())[1]]
        g = ipycytoscape.CytoscapeWidget()
        g.graph.add_graph_from_networkx(G, directed=True)
        g.set_style(STYLING)
        [n.data.pop('dendrite') for n in g.graph.nodes if not n.data['dendrite']]
        [n.data.pop('axon') for n in g.graph.nodes if not n.data['axon']]
        for n in g.graph.nodes:
            if ('axon' in n.data and 'dendrite' in n.data and
                n.data['axon'] and n.data['dendrite']):
                n.data['both-a-d'] = True
                n.data.pop('axon')
                n.data.pop('dendrite')

        display(g)

#===============================================================================
