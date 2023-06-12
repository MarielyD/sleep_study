from dash import Dash, html
import dash_bootstrap_components as dbc
from components.layout import create_layout

def main():
  app = Dash(external_stylesheets=[dbc.themes.LUX])
  server = app.server
  app.title='Sleep study '
  app.layout = create_layout(app)
  app.run_server(debug=True)

if __name__ == '__main__':
  main()