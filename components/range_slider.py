from dash import Dash, html, dcc
from .ids import *
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .util import read_file

def render(app):
  df = read_file()
  all_ages = df['Age'].unique()

  @app.callback(
    Output('output-container-range-slider', 'children'),
    [Input(RANGE_SLIDER, 'value')])
  
  def select_all_ages(value):
    return

  dropdown = html.Div(
    [
      dcc.RangeSlider(min = all_ages.min(), 
                      max = all_ages.max(), 
                      step = 1, 
                      value= [all_ages.min(), all_ages.max()], 
                      id=RANGE_SLIDER),
      html.Div(id='output-container-range-slider')
    ]
  )
  return dropdown