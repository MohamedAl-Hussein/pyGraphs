import json

from ud_graph import UndirectedGraph


demo_graph = UndirectedGraph(start_edges=['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG'])
data = json.dumps(demo_graph.__dict__)


def query_data(graph: UndirectedGraph) -> []:
    elements = list()
    for vertex in graph.get_vertices():
        config = {"data": {"id": vertex, "label": vertex}}
        elements.append(config)

    for src, dst in graph.get_edges():
        config = {"data": {"source": src, "target": dst}}
        elements.append(config)

    return elements
