from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import re

# Multipage imports
from app import app

layout = dbc.Container([
    
    
    dbc.Row([
    dbc.Col([
    ], md=1), 
    dbc.Col([
    html.Div(html.Img(src='/assets/hand.jpg',  style={ 'height': '300px'}), style={'display': 'flex', 'justify-content': 'right'}),
            ], md=5),
    dbc.Col([
    html.Div(dcc.Markdown('''
    **Автоматизирай корекцията на следните правила:**
    * Конвертирай английски(" ") в български кавички („ “)
    * Преобразувай й в ѝ
    * Преобразувай малко (-) в голямо (–) тире
        '''), style={'display': 'flex', 'justify-content': 'left'})], md=5),
    dbc.Col([
    ], md=1) 
    ], align="center", 
    ),
    
    
    dbc.Row([
    dbc.Col([
    ], md=1), 
    dbc.Col([
    html.Div(
    dcc.Textarea(
        id='textarea-wrong-quotes',
        value='Конвертирай английски в български кавички - " "',
        maxLength='10000',
        style={'width': '100%', 'height': 400, 'padding': '15px', 'resize' : 'none', 'border-radius': '10px', 'whiteSpace': 'pre-line', 'padding-bottom': '40px',})),
            ], md=5),
    dbc.Col([
    dcc.Textarea(id='textarea-output', readOnly=True, style={'height': 400, 'width': '100%', 'backgroundColor': '#EBF3FE',  'padding': '15px', 'resize' : 'none', 'border-radius': '10px'}),
            ], md=5), 
    dbc.Col([
    ], md=1), 
        ], align="center", 
        style={ "margin-top": "5px", "margin-bottom": "0px"}
        ),
    dbc.Row([
    dbc.Col([
    html.Div(id='character-count', style={'whiteSpace': 'pre-line'}),
            ], md=6),
    dbc.Col([
            ], md=6) 
        ], align="center", 
        style={ "margin-top": "0px", "margin-bottom": "0px"}
        ),
    
], fluid=True)

# Output the number of characters
@app.callback(
    Output('character-count', 'children'),
    Input('textarea-wrong-quotes', 'value')
)
def update_output(value):
    number_characters = len(value)
    return '{} / 10,000'.format(number_characters)
    
# Replace all wrong style quotes to Bulgarian style quotes
@app.callback(
    Output('textarea-output', 'value'),
    Input('textarea-wrong-quotes', 'value')
)
def update_output(value):
    replaced_value = re.sub(r'\"(.*?)\"', r'„\1“', value)
    replaced_value = re.sub(r'\“(.*?)\”', r'„\1“', replaced_value)
    replaced_i = replaced_value.replace(" й ", " ѝ ")
    change_hypen = replaced_i.replace(" - ", " – ")
    return change_hypen

