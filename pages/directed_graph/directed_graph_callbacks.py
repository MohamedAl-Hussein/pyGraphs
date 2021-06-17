import dash
from dash.dependencies import Input, Output, State

import json

from app import app
from pages.directed_graph.directed_graph_data import query_data
from d_graph import DirectedGraph


@app.callback(
    Output("dGraph", "elements"),
    Output("src-node", "value"),
    Output("dst-node", "value"),
    Output("edge-weight", "value"),
    Output("dGraphData", "data"),
    Input("btn-add-edge", "n_clicks_timestamp"),
    Input("btn-remove-edge", "n_clicks_timestamp"),
    Input("btn-add-vertex", "n_clicks_timestamp"),
    State("dGraphData", "data"),
    State("src-node", "value"),
    State("dst-node", "value"),
    State("edge-weight", "value")
)
def update_graph(btn_add_edge, btn_remove_edge, btn_add_vertex, data, src, dst, weight):
    _graph = DirectedGraph()
    _graph.__dict__ = json.loads(data)
    btn_id = dash.callback_context.triggered[0]["prop_id"].split('.')[0]
    if btn_id == "btn-add-edge" and btn_add_edge:
        _graph.add_edge(int(src or 0), int(dst or 0), int(weight or 0))
    elif btn_id == "btn-remove-edge" and btn_remove_edge:
        _graph.remove_edge(int(src or 0), int(dst or 0))
    elif btn_id == "btn-add-vertex" and btn_add_vertex:
        _graph.add_vertex()

    elements = query_data(_graph)
    return elements, str(), str(), str(), json.dumps(_graph.__dict__)
