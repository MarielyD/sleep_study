from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from .ids import *
from .util import read_file

def render(app):
  df = read_file()
  @app.callback(
    Output(PIE_CHART, "children"),
    [
      Input(BMI_DROPDOWN, "value"),
      Input(GENDER_DROPDOWN, "value"),
    ],
  )
  def update_pie_chart(bmi, genders):
    filtered_data = df.query("`BMI Category`in @bmi and `Gender` in @genders")
    if filtered_data.shape[0] == 0:
        return html.Div("No data is selected")

    fig = px.pie(
        filtered_data,
        values= "Sleep Duration",
        names= "Sleep Disorder",
        hole=0.4)
    return html.Div(dcc.Graph(figure=fig), id=PIE_CHART)
  
  return html.Div(id=PIE_CHART)
