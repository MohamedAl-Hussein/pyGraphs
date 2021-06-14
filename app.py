import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_cytoscape as cyto
import dash_html_components as html
import json
from dash.dependencies import Input, Output, State

from d_graph import DirectedGraph
from ud_graph import UndirectedGraph


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


def ud_graph_elements(graph: UndirectedGraph) -> []:
    elements = list()
    for vertex in graph.get_vertices():
        config = {"data": {"id": vertex, "label": vertex}}
        elements.append(config)

    for src, dst in graph.get_edges():
        config = {"data": {"source": src, "target": dst}}
        elements.append(config)

    return elements


def d_graph_elements(graph: DirectedGraph) -> []:
    elements = list()
    for vertex in graph.get_vertices():
        config = {"data": {"id": str(vertex), "label": str(vertex)}}
        elements.append(config)

    for src, dst, weight in graph.get_edges():
        config = {"data": {"source": str(src), "target": str(dst), "weight": weight}}
        elements.append(config)

    return elements


graph = UndirectedGraph(start_edges=['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG'])
edges = [(0, 1, 19), (0, 6, 13), (0, 8, 14), (2, 4, 10), (3, 4, 14), (7, 10, 14), (11, 3, 13), (12, 1, 20), (12, 2, 7),
         (12, 4, 18), (12, 10, 13), (12, 11, 4)]
digraph = DirectedGraph(start_edges=edges)
digraphData = json.dumps(digraph.__dict__)
graphData = json.dumps(graph.__dict__)

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Data Structure / Algorithm", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Directed Graph", href="/digraph", active="exact"),
                dbc.NavLink("Undirected Graph", href="/graph", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

directed_graph = dbc.Row([
    dbc.Col(
        cyto.Cytoscape(
            id="dGraph",
            layout={"name": "cose"},
            style={"width": "100%", "height": "400px"},
            elements=d_graph_elements(digraph),
            stylesheet=[
                {
                    "selector": "node",
                    "style": {
                        "content": "data(label)",
                        "text-halign": "center",
                        "text-valign": "center",
                        "width": "30px",
                        "height": "30px",
                        "shape": "circle"
                    }
                },
                {
                    "selector": "edge",
                    "style": {
                        "label": "data(weight)",
                        "text-rotation": "autorotate",
                        "text-margin-y": "10px",
                        "text-halign": "top",
                        "text-valign": "top",
                        "curve-style": "bezier",
                        "target-arrow-color": "red",
                        "target-arrow-shape": "triangle"
                    }
                },
                {
                    "selector": "[weight > 0]",
                    "style": {
                        "line-color": "blue"
                    }
                }
            ]
        ),
        width=9
    ),
    dbc.Col([
        dbc.Row(
            dbc.FormGroup([
                dbc.Label("Add Edge"),
                dbc.Input(type="text", id="src-node"),
                dbc.Input(type="text", id="dst-node"),
                dbc.Input(type="text", id="edge-weight"),
                dbc.Button("Add", id="btn-add-edge", n_clicks_timestamp=0, color="primary"),
                dbc.Button("Remove", id="btn-remove-edge", n_clicks_timestamp=0, color="primary")
            ])
        ),
        dbc.Row(
            dbc.FormGroup([
                dbc.Label("Add Vertex"),
                dbc.Button("Add", id="btn-add-vertex", color="primary")
            ])
        )
    ], width=3)
])

undirected_graph = dbc.Row([
    dbc.Col(
        cyto.Cytoscape(
            id="udGraph",
            layout={"name": "cose"},
            style={"width": "100%", "height": "400px"},
            elements=ud_graph_elements(graph),
            stylesheet=[
                {
                    "selector": "node",
                    "style": {
                        "content": "data(label)",
                        "text-halign": "center",
                        "text-valign": "center",
                        "width": "30px",
                        "height": "30px",
                        "shape": "circle"
                    }
                },
                {
                    "selector": "edge",
                    "style": {
                        "curve-style": "bezier",
                    }
                }
            ]
        ),
        width=9
    ),
    dbc.Col([
        dbc.Row(
            dbc.FormGroup([
                dbc.Label("Add Edge"),
                dbc.Input(type="text", id="ud-src-node"),
                dbc.Input(type="text", id="ud-dst-node"),
                dbc.Button("Add", id="ud-btn-add-edge", n_clicks_timestamp=0, color="primary"),
                dbc.Button("Remove", id="ud-btn-remove-edge", n_clicks_timestamp=0, color="primary")
            ])
        ),
        dbc.Row(
            dbc.FormGroup([
                dbc.Label("Add Vertex"),
                dbc.Input(type="text", id="ud-vertex"),
                dbc.Button("Add", id="ud-btn-add-vertex", color="primary"),
                dbc.Button("Remove", id="ud-btn-remove-vertex", color="primary")
            ])
        )
    ], width=3)
])

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
    dcc.Store(id="dGraphData", data=digraphData),
    dcc.Store(id="udGraphData", data=graphData)
])


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return html.H1("Home Page")
    elif pathname == "/digraph":
        return directed_graph
    elif pathname == "/graph":
        return undirected_graph

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


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
def update_dgraph(btn_add_edge, btn_remove_edge, btn_add_vertex, data, src, dst, weight):
    _graph = DirectedGraph()
    _graph.__dict__ = json.loads(data)
    btn_id = dash.callback_context.triggered[0]["prop_id"].split('.')[0]
    if btn_id == "btn-add-edge" and btn_add_edge:
        _graph.add_edge(int(src or 0), int(dst or 0), int(weight or 0))
    elif btn_id == "btn-remove-edge" and btn_remove_edge:
        _graph.remove_edge(int(src or 0), int(dst or 0))
    elif btn_id == "btn-add-vertex" and btn_add_vertex:
        _graph.add_vertex()

    elements = d_graph_elements(_graph)
    return elements, str(), str(), str(), json.dumps(_graph.__dict__)


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
def update_graph_elements(btn_add_edge, btn_remove_edge, btn_add_vertex, btn_remove_vertex, data, src, dst, v):
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

    elements = ud_graph_elements(_graph)
    return elements, str(), str(), str(), json.dumps(_graph.__dict__)


if __name__ == "__main__":
    app.run_server(debug=True)
