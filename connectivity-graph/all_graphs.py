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

import math
import os

#===============================================================================

import igraph as ig
import networkx as nx

#===============================================================================

from connectivity_graph import ConnectivityKnowledge

#===============================================================================

MODELS = [
    'https://apinatomy.org/uris/models/bronchomotor',
    'https://apinatomy.org/uris/models/ard-arm-cardiac',
    'https://apinatomy.org/uris/models/bolser-lewis',
    'https://apinatomy.org/uris/models/sawg-distal-colon',
    'https://apinatomy.org/uris/models/keast-bladder',
    'https://apinatomy.org/uris/models/pancreas',
    'https://apinatomy.org/uris/models/sawg-stomach',
    'https://apinatomy.org/uris/models/spleen',
]

#===============================================================================

def graph_from_knowledge(store, knowledge):
    G = nx.Graph()
    for n, pair in enumerate(knowledge.get('connectivity', [])):
        nodes = (store.node_id(pair[0]),
                 store.node_id(pair[1]))
        if (nodes[0] != nodes[1]):
            G.add_edge(*nodes, directed=True, id=n)
            n += 1
    return G


def list_paths(scicrunch_release, graph_dir=None):
    store = ConnectivityKnowledge(scicrunch_release=scicrunch_release)
    if graph_dir is not None and not os.path.exists(graph_dir):
        os.makedirs(graph_dir)

    log_output = []
    def log(msg):
        print(msg, flush=True)
        if graph_dir is not None:
            log_output.append(msg)

    log(store.scicrunch.sparc_api_endpoint)
    for model in sorted(MODELS):
        model_name = model.rsplit('/', 1)[-1]
        paths = store.entity_knowledge(model)['paths']
        if len(paths) == 0:
            log(f'{model_name}: No paths...')
        else:
            log(f'{model_name}: {len(paths)} paths')
        for path_id in sorted([path['id'] for path in paths]):
            path_knowledge = store.entity_knowledge(path_id)
            phenotypes = path_knowledge.get('phenotypes', [])
            graph = graph_from_knowledge(store, path_knowledge)
            components = list(nx.connected_components(graph))
            if len(components) == 0:
                log(f'{model_name}: {path_id}: NO PATH, {phenotypes}')
            else:
                log(f'{model_name}: {path_id}: {len(components)} components, {phenotypes}')
            for n, nodes in enumerate(components):
                if graph_dir is not None:
                    G = graph.subgraph(nodes)
                    g = ig.Graph.from_networkx(G)
                    layout = g.layout("kamada_kawai")
                    g.vs["label"] = g.vs["_nx_name"]
                    pdf_file = f'{graph_dir}/{model_name}_{path_id[6:]}_{n}.pdf'
                    graph_size = g.vcount()
                    box_size = 250*math.ceil(((max(graph_size, 4)/4)**0.75))
                    ig.plot(g, pdf_file, layout=layout, vertex_size=40, bbox=(box_size, box_size),
                            edge_color='pink', edge_width=5, vertex_label_color='navy',
                            vertex_label_size=9, vertex_color='#80f0f0', margin=50)
    if graph_dir is not None:
        with open(f'{graph_dir}/all_graphs.txt', 'w') as fp:
            fp.write('\n'.join(log_output))
            fp.write('\n')

#==============================================================================

if __name__ == '__main__':
    from mapknowledge.scicrunch import SCICRUNCH_PRODUCTION, SCICRUNCH_STAGING

    list_paths(SCICRUNCH_STAGING, graph_dir='staging_graphs')

#===============================================================================

