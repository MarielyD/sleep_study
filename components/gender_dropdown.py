from dash import Dash, html, dcc
from .ids import *
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .util import read_file

def render(app):
  df = read_file()
  all_genders = df['Gender'].unique()

  @app.callback(
    Output(GENDER_DROPDOWN, "value"),
    Input(SELECT_ALL_GENDERS , "n_clicks")
  )
  def select_all_genders(n):
    return all_genders

  dropdown = html.Div(
    [
      html.Br(),
      html.H6("Genders"),
      dcc.Dropdown(
        id=GENDER_DROPDOWN,
        options=[{"label":gender, "value":gender} for gender in all_genders],
        multi=True,
      ),
      html.Button(
        id=SELECT_ALL_GENDERS,
        children=["Select All"],
        className="dropdown-button",
        n_clicks=0
      ),
    ]
  )
  return dropdown