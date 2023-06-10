from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from dash import Dash, dcc, html
import pandas as pd
from .ids import *
from .util import read_file

def render(app):
  df = read_file()
  fig = px.scatter(df, x="Age", y="Sleep Duration", color="BMI Category", title='Sleep duration vs BMI depending on age')
  return html.Div(dcc.Graph(figure=fig))