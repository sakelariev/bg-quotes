from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import re

# Multipage imports
from app import app


# Try to highlight the string values
def entbox(children):
    return html.Mark(children, style={
        "background": "#FFC04E",
        "padding": "0.1em 0.05em 0.1em 0.05em",
        # "margin": "0 0.15em",
        "line-height": "1",
        "border-radius": "0.15em",
    })


def entity(children):
    if type(children) is str:
        children = [children]
    return entbox(children)


def render(string):
    children = []
    last_idx = 0
    # for match in re.finditer(r'(\„)(.*?)(\“)|(ѝ)|(–)', string):
    for match in re.finditer(r'(„)|(“)|(ѝ)|(–)', string):
        # selected_groups = match.groups()
        # selected_groups = list(selected_groups)
        # for i in range(len(selected_groups)):
        #     if selected_groups[i] is None:
        #         selected_groups[i] = ''
        # selected_groups = selected_groups[:1] + selected_groups[2:]
        # print(selected_groups.start())
        # print(selected_groups.end())
        start_char = match.start()
        end_char = match.end()
        children.append(string[last_idx:start_char])
        children.append(entity(string[start_char:end_char]))
        last_idx = end_char
    children.append(string[last_idx:])
    return children




layout = dbc.Container([
    
    
    dbc.Row([
    dbc.Col([
    ], md=1), 
    dbc.Col([
    html.Div(html.Img(src='/assets/hand.jpg',  style={ 'height': '300px'}), style={'display': 'flex', 'justify-content': 'flex-end'}),
            ], md=5),
    dbc.Col([
    html.Div(dcc.Markdown('''
    **Автоматизирай следните правила:**
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
        maxLength='40000',
        style={'width': '100%', 'height': 400, 'padding': '15px', 'resize' : 'none', 'border-radius': '10px', 'whiteSpace': 'pre-line', 'padding-bottom': '40px',}),
        style={'padding-top': '10px'}),
            ], md=5),
    dbc.Col([
    html.Div([
        
    html.Div(id='textarea-output', style={'height': 400, 'width': '100%', 'backgroundColor': '#EBF3FE',  'padding': '15px', 'resize' : 'none', 'border-radius': '10px', 'whiteSpace': 'pre-line', 'overflow-y':'auto', 'overflow-x': 'hidden'}),
    dcc.Clipboard(
        target_id="textarea-output",
        id="copy",
        style={"position": "absolute","top": 7,"right": 7,"fontSize": 20},
    ),
    
    ], style={"position": "relative"},)
    # dcc.Textarea(id='textarea-output', readOnly=True, style={'height': 400, 'width': '100%', 'backgroundColor': '#EBF3FE',  'padding': '15px', 'resize' : 'none', 'border-radius': '10px'}),
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
    return '{} / 40,000'.format(number_characters)
    
# Replace all wrong style quotes to Bulgarian style quotes
@app.callback(
    Output('textarea-output', 'children'),
    Input('textarea-wrong-quotes', 'value')
)
def update_output(value):
    replaced_value = re.sub(r'\"(.*?)\"', r'„\1“', value)
    replaced_value = re.sub(r'\“(.*?)\”', r'„\1“', replaced_value)
    replaced_i = replaced_value.replace(" й ", " ѝ ")
    change_hypen = replaced_i.replace(" - ", " – ")
    children=render(change_hypen)
    return children



# @app.callback(
#     Output("copy", "content"),
#     Input("copy", "n_clicks"),
#     State("textarea-output", "children"),
# )
# def custom_copy(_, text):
#     end_text = []
#     for element in text:
#         print(element)
#         if type(element) is str:
#             end_text.append(element)
#         elif type(element) is dict:
#             edited_element = element['props']['children'][0]
#             end_text.append(edited_element)
#     end_string = ''.join(end_text)
#     print(end_string)
#     return end_string
    
    