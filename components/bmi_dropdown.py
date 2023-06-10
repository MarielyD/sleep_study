from dash import Dash, html, dcc
from .ids import *
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .util import read_file

def render(app):
  df = read_file()
  all_bmis = df['BMI Category'].unique()

  @app.callback(
    Output(BMI_DROPDOWN, "value"),
    Input(SELECT_ALL_BMIS , "n_clicks")
  )
  def select_all_bmis(n):
    return all_bmis

  dropdown = html.Div(
    [
      html.Br(),
      html.H6("BMI Category"),
      dcc.Dropdown(
        id=BMI_DROPDOWN,
        options=[{"label":bmi, "value":bmi} for bmi in all_bmis],
        multi=True,
      ),
      html.Button(
        id=SELECT_ALL_BMIS ,
        children=["Select All"],
        className="dropdown-button",
        n_clicks=0
      ),
    ]
  )
  return dropdown