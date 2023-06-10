import plotly.express as px
from dash import Dash, dcc, html
import pandas as pd
from .ids import *
from .util import read_file

def render(app):
  df = read_file()
  fig = px.scatter(df, x="Age", y="Heart Rate", color="BMI Category", title='Heart Rate vs BMI depending on age')
  return html.Div(dcc.Graph(figure=fig))

