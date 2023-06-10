from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import get_gender_duration_avg, get_occupation_duration_avg,get_age_duration_avg

def render(app):
  @app.callback(
    Output(SLEEP_DURATION, 'children'),
    Input(CATEGORY, 'value')
  )
  def update_bar_chart(dropdown):
    if dropdown == 'Gender':
      df = get_gender_duration_avg()
      fig = px.bar(
        df,
        x="Gender",
        y="Sleep Duration",
        color="Gender",
        title="Average duration of sleep by gender (hours)")
      return html.Div(dcc.Graph(figure=fig), id=SLEEP_DURATION)
    elif dropdown == 'Occupation':
      df = get_occupation_duration_avg()
      fig = px.bar(
        df,
        x="Sleep Duration",
        y="Occupation",
        color="Occupation",
        orientation='h',
        title="Average duration of sleep by occupation (hours)")
      return html.Div(dcc.Graph(figure=fig), id=SLEEP_DURATION)
    elif dropdown == 'Age':
      df =get_age_duration_avg()
      fig = px.line(
        df,
        x="Age",
        y="Sleep Duration",
        title="Average duration of sleep by age (hours)")
      return html.Div(dcc.Graph(figure=fig), id=SLEEP_DURATION)
    return html.Div(id=SLEEP_DURATION)