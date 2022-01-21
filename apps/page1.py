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
    html.Div(html.Img(src='/assets/hand.jpg',  style={ 'height': '300px'}), style={'display': 'flex', 'justify-content': 'center'}),
            ], md=10),
    dbc.Col([
    ], md=1) 
    ], align="center", 
    ),
    
    
    dbc.Row([
    dbc.Col([
    ], md=2), 
    dbc.Col([
    html.Div(
    dcc.Textarea(
        id='textarea-wrong-quotes',
        value='Конвертирай английски в български кавички - " "',
        maxLength='5000',
        style={'width': '100%', 'height': 400, 'padding': '15px', 'resize' : 'none', 'border-radius': '10px', 'whiteSpace': 'pre-line', 'padding-bottom': '40px',})),
            ], md=4),
    dbc.Col([
    dcc.Textarea(id='textarea-output', readOnly=True, style={'height': 400, 'width': '100%', 'backgroundColor': '#EBF3FE',  'padding': '15px', 'resize' : 'none', 'border-radius': '10px'}),
            ], md=4), 
    dbc.Col([
    ], md=2), 
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
    return '{} / 5000'.format(number_characters)
    
# Replace all wrong style quotes to Bulgarian style quotes
@app.callback(
    Output('textarea-output', 'value'),
    Input('textarea-wrong-quotes', 'value')
)
def update_output(value):
    replaced_value = re.sub(r'\"(.*?)\"', r'„\1“', value)
    return replaced_value


if __name__ == '__main__':
    app.run_server(debug=True)