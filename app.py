from dash import Dash, html
import dash_bootstrap_components as dbc
from components.layout import create_layout


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server
app.title='Sleep study '
app.layout = create_layout(app)


if __name__ == '__main__':
  app.run_server(debug=True)