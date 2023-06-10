from dash import Dash,html,dcc 
import dash_bootstrap_components as dbc
import pandas as pd
from .ids import *
from .util import read_file

def render(app):
  return html.Div([
    dcc.Dropdown(
      options=[
        {'label': 'Gender', 'value': 'Gender'},
        {'label': 'Age', 'value': 'Age'},
        {'label': 'Occupation', 'value': 'Occupation'},
       ],
      placeholder= "Choose a category",
      className="mb-3",
      value = "Gender",
      id = CATEGORY,
      multi =False
    )
  ])