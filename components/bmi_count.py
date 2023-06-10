from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import bmi_count

def render(app):
  df = bmi_count()
  fig = px.pie(
    df,
    values= df.values,
    names= df.index,
    title="BMI Category",
    color_discrete_sequence=px.colors.sequential.Greens_r)
  return html.Div(dcc.Graph(figure=fig))