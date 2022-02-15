from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

FA = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
external_stylesheets = [dbc.themes.SKETCHY, FA]

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'Граматичен асистент'