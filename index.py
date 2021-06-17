from app import app, server

from environment.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK
from pages.directed_graph.directed_graph_callbacks import query_data as d_query_data
from pages.undirected_graph.undirected_graph_callbacks import query_data as ud_query_data
from routes import render_page_content


if __name__ == "__main__":
    app.run_server(
        host=APP_HOST,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
    )
