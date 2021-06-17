import json

from d_graph import DirectedGraph


edges = [(0, 1, 19), (0, 6, 13), (0, 8, 14), (2, 4, 10), (3, 4, 14), (7, 10, 14), (11, 3, 13), (12, 1, 20), (12, 2, 7),
         (12, 4, 18), (12, 10, 13), (12, 11, 4)]
demo_graph = DirectedGraph(start_edges=edges)
data = json.dumps(demo_graph.__dict__)


def query_data(graph: DirectedGraph) -> []:
    elements = list()
    for vertex in graph.get_vertices():
        config = {"data": {"id": str(vertex), "label": str(vertex)}}
        elements.append(config)

    for src, dst, weight in graph.get_edges():
        config = {"data": {"source": str(src), "target": str(dst), "weight": weight}}
        elements.append(config)

    return elements
