import dash_bootstrap_components as dbc
import dash_html_components as html

from utils.constants import URL_DIRECTED_GRAPH, URL_HOME, URL_UNDIRECTED_GRAPH


sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Data Structure / Algorithm", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href=URL_HOME, active="exact"),
                dbc.NavLink("Directed Graph", href=URL_DIRECTED_GRAPH, active="exact"),
                dbc.NavLink("Undirected Graph", href=URL_UNDIRECTED_GRAPH, active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar"
)
