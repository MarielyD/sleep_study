from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import stress_level_count, read_file

def render(app):
  df = stress_level_count()
  fig = px.pie(
    df,
    values= df.values,
    names= df.index,
    title="Stress Level (scale: 1-10)",
    color_discrete_sequence=px.colors.sequential.Reds_r)
  return html.Div(dcc.Graph(figure=fig))