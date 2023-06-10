from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import read_file

def render(app):
  df = read_file()
  @app.callback(
    Output(AGE_PIE_CHART, "children"),
    [
      Input(RANGE_SLIDER, "value")
    ],
  )
  def update_pie_chart(ages):
    filtered_data = df.query(" `Age` >= @ages[0] and `Age` <= @ages[1]")
    if filtered_data.shape[0] == 0:
        return html.Div("No data is selected")

    fig = px.pie(
        filtered_data,
        values= "Sleep Duration",
        names= "Sleep Disorder",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Blues_r)
    return html.Div(dcc.Graph(figure=fig), id=AGE_PIE_CHART)
  
  return html.Div(id=AGE_PIE_CHART)