from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import get_gender_exercise_avg, get_occupation_exercise_avg, get_age_exercise_avg

def render(app):
  @app.callback(
    Output(PHYSICAL_ACTIVITY, 'children'),
    Input(CATEGORY, 'value')
  )
  def update_bar_chart(dropdown):
    if dropdown == 'Gender':
      df = get_gender_exercise_avg()
      fig = px.bar(
        df,
        x="Gender",
        y="Physical Activity Level",
        color="Gender",
        title="Average physical activity level by gender (minutes)")
      return html.Div(dcc.Graph(figure=fig), id=PHYSICAL_ACTIVITY)
    elif dropdown == 'Occupation':
      df = get_occupation_exercise_avg()
      fig = px.bar(
        df,
        x="Physical Activity Level",
        y="Occupation",
        color="Occupation",
        orientation='h',
        title="Average physical activity level by occupation (minutes)")
      return html.Div(dcc.Graph(figure=fig), id=PHYSICAL_ACTIVITY)
    elif dropdown == 'Age':
      df =get_age_exercise_avg()
      fig = px.line(
        df,
        x="Age",
        y="Physical Activity Level",
        title="Average physical activity level by age (minutes)")
      return html.Div(dcc.Graph(figure=fig), id=PHYSICAL_ACTIVITY)
    return html.Div(id=PHYSICAL_ACTIVITY)
  