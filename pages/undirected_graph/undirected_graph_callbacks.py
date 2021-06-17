import dash
from dash.dependencies import Input, Output, State

import json

from app import app
from pages.undirected_graph.undirected_graph_data import query_data
from ud_graph import UndirectedGraph


@app.callback(
    Output("udGraph", "elements"),
    Output("ud-src-node", "value"),
    Output("ud-dst-node", "value"),
    Output("ud-vertex", "value"),
    Output("udGraphData", "data"),
    Input("ud-btn-add-edge", "n_clicks_timestamp"),
    Input("ud-btn-remove-edge", "n_clicks_timestamp"),
    Input("ud-btn-add-vertex", "n_clicks_timestamp"),
    Input("ud-btn-remove-vertex", "n_clicks_timestamp"),
    State("udGraphData", "data"),
    State("ud-src-node", "value"),
    State("ud-dst-node", "value"),
    State("ud-vertex", "value")
)
def update_graph(btn_add_edge, btn_remove_edge, btn_add_vertex, btn_remove_vertex, data, src, dst, v):
    _graph = UndirectedGraph()
    _graph.__dict__ = json.loads(data)
    btn_id = dash.callback_context.triggered[0]["prop_id"].split('.')[0]
    if btn_id == "ud-btn-add-edge" and btn_add_edge:
        if src is not None and dst is not None:
            _graph.add_edge(src, dst)
    elif btn_id == "ud-btn-remove-edge" and btn_remove_edge:
        if src is not None and dst is not None:
            _graph.remove_edge(src, dst)
    elif btn_id == "ud-btn-add-vertex" and btn_add_vertex:
        if v is not None:
            _graph.add_vertex(v)
    elif btn_id == "ud-btn-remove-vertex" and btn_remove_vertex:
        if v is not None:
            _graph.remove_vertex(v)

    elements = query_data(_graph)
    return elements, str(), str(), str(), json.dumps(_graph.__dict__)
