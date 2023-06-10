from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import sleep_disorder_count

def render(app):
  df = sleep_disorder_count()
  fig = px.pie(
    df,
    values= df.values,
    names= df.index,
    title="Sleep Disorder",
    color_discrete_sequence=px.colors.sequential.Purp_r)
  return html.Div(dcc.Graph(figure=fig))