from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import get_gender_sleep_avg, get_occupation_sleep_avg, get_age_sleep_avg

def render(app):
  @app.callback(
    Output(SLEEP_QUALITY, 'children'),
    Input(CATEGORY, 'value')
  )
  def update_bar_chart(dropdown):
    if dropdown == 'Gender':
      df = get_gender_sleep_avg()
      fig = px.bar(
        df,
        x="Gender",
        y="Quality of Sleep",
        color="Gender",
        title="Average quality of sleep by gender")
      return html.Div(dcc.Graph(figure=fig), id=SLEEP_QUALITY)
    elif dropdown == 'Occupation':
      df = get_occupation_sleep_avg()
      fig = px.bar(
        df,
        x="Quality of Sleep",
        y="Occupation",
        color="Occupation",
        orientation='h',
        title="Average quality of sleep by occupation")
      return html.Div(dcc.Graph(figure=fig), id=SLEEP_QUALITY)
    elif dropdown == 'Age':
      df = get_age_sleep_avg()
      fig = px.line(
        df,
        x="Age",
        y="Quality of Sleep",
        title="Average quality of sleep by age")
      return html.Div(dcc.Graph(figure=fig), id=SLEEP_QUALITY)
    return html.Div(id=SLEEP_QUALITY)