from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import get_gender_stress_level_avg, get_occupation_stress_level_avg, get_age_stress_level_avg

def render(app):
  @app.callback(
    Output(STRESS_LEVEL, 'children'),
    Input(CATEGORY, 'value')
  )
  def update_bar_chart(dropdown):
    if dropdown == 'Gender':
      df = get_gender_stress_level_avg()
      fig = px.bar(
        df,
        x="Gender",
        y="Stress Level",
        color="Gender",
        title="Average stress level by gender")
      return html.Div(dcc.Graph(figure=fig), id=STRESS_LEVEL)
    elif dropdown == 'Occupation':
      df = get_occupation_stress_level_avg()
      fig = px.bar(
        df,
        x="Stress Level",
        y="Occupation",
        color="Occupation",
        orientation='h',
        title="Average stress level by occupation")
      return html.Div(dcc.Graph(figure=fig), id=STRESS_LEVEL)
    elif dropdown == 'Age':
      df =get_age_stress_level_avg()
      fig = px.line(
        df,
        x="Age",
        y="Stress Level",
        title="Average stress level by age")
      return html.Div(dcc.Graph(figure=fig), id=STRESS_LEVEL)
    return html.Div(id=STRESS_LEVEL)