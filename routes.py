import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from pages.directed_graph import directed_graph
from pages.home import home
from pages.undirected_graph import undirected_graph
from utils.constants import URL_DIRECTED_GRAPH, URL_HOME, URL_UNDIRECTED_GRAPH


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == URL_HOME:
        return home.layout
    elif pathname == URL_DIRECTED_GRAPH:
        return directed_graph.layout
    elif pathname == URL_UNDIRECTED_GRAPH:
        return undirected_graph.layout

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
