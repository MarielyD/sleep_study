from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import sleep_quality_count

def render(app):
  df = sleep_quality_count()
  fig = px.pie(
    df,
    values= df.values,
    names= df.index,
    title="Quality of Sleep (scale: 1-10)",
    color_discrete_sequence=px.colors.sequential.Blues_r)
  return html.Div(dcc.Graph(figure=fig))