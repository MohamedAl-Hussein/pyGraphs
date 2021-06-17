import dash
import dash_bootstrap_components as dbc
import flask

from layout.layout import layout


server = flask.Flask(__name__)

app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

server = app.server
