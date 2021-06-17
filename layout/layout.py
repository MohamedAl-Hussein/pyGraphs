import dash_core_components as dcc
import dash_html_components as html

from layout.sidebar.sidebar import sidebar


content = html.Div(id="page-content")

layout = html.Div([dcc.Location(id="url"), sidebar, content])
