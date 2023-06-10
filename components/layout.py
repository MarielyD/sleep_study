from dash import dcc, html
import dash_bootstrap_components as dbc
from .ids import *
from components import (
    age_sleep_scatter,
    age_pie_chart,
    range_slider,
    gender_dropdown,
    bmi_dropdown,
    dropdown,
    sleep_quality,
    sleep_duration,
    physical_activity,
    sleep_quality_total,
    stress_level,
    stress_level_total,
    bmi_count,
    sleep_disorder_count,
    age_stress_scatter,
    pie_chart
)

def create_layout(app):
    return dbc.Container([
        html.H1( "Sleep and Lifestyle Data 🌙", style={'textAlign': 'center', 'marginTop': '30px'}),
        dbc.Row([
            dbc.Col(sleep_quality_total.render(app), lg=6),
            dbc.Col(stress_level_total.render(app), lg=6)
        ]),
        dbc.Row([
            dbc.Col(bmi_count.render(app), lg=6),
            dbc.Col(sleep_disorder_count.render(app), lg=6)
        ]),
        html.H3( "Choose a category", style={'textAlign': 'center', 'marginTop': '30px'}),
        dbc.Row([dropdown.render(app)]),
        dbc.Row([
            dbc.Col(sleep_quality.render(app), lg=6, id=SLEEP_QUALITY),
            dbc.Col(sleep_duration.render(app), lg=6, id=SLEEP_DURATION),
        ]),
        dbc.Row([
            dbc.Col(physical_activity.render(app), lg=6, id=PHYSICAL_ACTIVITY),
            dbc.Col(stress_level.render(app), lg=6, id=STRESS_LEVEL)
        ]),
        dbc.Row([
            html.H3("Filter by Age Range", style={'textAlign': 'center', 'marginTop': '30px'}),
            dbc.Col(
              dbc.Row([
                range_slider.render(app),
              ]), lg= 12),
            dbc.Col(age_pie_chart.render(app), lg =12),
        ]),
        dbc.Row([
            dbc.Col(age_sleep_scatter.render(app), lg=6),
            dbc.Col(age_stress_scatter.render(app), lg=6)
        ]),
        dbc.Row([
            html.H3("Sleep Disorders and Sleep Duration percentages", style={'textAlign': 'center', 'marginTop': '30px'}),
            dbc.Col(pie_chart.render(app), lg =6),
            dbc.Col(
              dbc.Row([
                bmi_dropdown.render(app),
                gender_dropdown.render(app),
              ]), lg= 6),
        ]),
    ])