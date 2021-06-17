import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from pages.undirected_graph.undirected_graph_data import data, demo_graph, query_data


layout = dbc.Row([
    dbc.Col(
        cyto.Cytoscape(
            id="udGraph",
            layout={"name": "cose"},
            style={"width": "100%", "height": "400px"},
            elements=query_data(demo_graph),
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
    ], width=3),
    dcc.Store(id="udGraphData", data=data)
])
