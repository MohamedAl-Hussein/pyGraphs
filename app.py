import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_cytoscape as cyto
import dash_html_components as html
from dash.dependencies import Input, Output

from d_graph import DirectedGraph
from ud_graph import UndirectedGraph


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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

directed_graph = cyto.Cytoscape(
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
)

undirected_graph = cyto.Cytoscape(
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
)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.H1("Home Page")
    elif pathname == "/digraph":
        return html.Div(directed_graph)
    elif pathname == "/graph":
        return html.Div(undirected_graph)

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)
