import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from pages.directed_graph.directed_graph_data import data, demo_graph, query_data


layout = dbc.Row([
    dbc.Col(
        cyto.Cytoscape(
            id="dGraph",
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
    ], width=3),
    dcc.Store(id="dGraphData", data=data)
])
