from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

from app import app, server
from apps import page1



'''
If Google Analytics is needed - use below code (all projects shoud ideally have this)
'''
# app.index_string = """<!DOCTYPE html>
# <html>
#     <head>
#         <!-- Global site tag (gtag.js) - Google Analytics -->
#         <script async src="https://www.googletagmanager.com/gtag/js?id=G-NV0FPPWHYK"></script>
#         <script>
#           window.dataLayer = window.dataLayer || [];
#           function gtag(){dataLayer.push(arguments);}
#           gtag('js', new Date());
#         
#           gtag('config', 'G-NV0FPPWHYK');
#         </script>
#         {%metas%}
#         <title>{%title%}</title>
#         {%favicon%}
#         {%css%}
#     </head>
#     <body>
#         {%app_entry%}
#         <footer>
#             {%config%}
#             {%scripts%}
#             {%renderer%}
#         </footer>
#     </body>
# </html>"""


app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        dbc.NavbarSimple(
        children=[
            # dbc.NavItem(dbc.NavLink("Конвертирай в български кавички", href="/apps/page-1", id='page1-link')),
            # dbc.NavItem(dbc.NavLink("Page 2", href="/apps/page-2", id='google-link')),
            # dbc.NavItem(dbc.NavLink("Page 3", href="/apps/page-3", id='table-link')),
        ],
        brand="Writing assistant",
        color="#FFC04E",
        dark=False,
        id = "navbar-index",
        brand_href="/",
    ),
        html.Div(id='page-content'),
        html.Div(html.P("2022 © Авторът на този уебсайт го създаде, за да може приятелката му да не губи време в ръчно копиране на кавички", id='footer'), id='footer_container'),
        
    ])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/page-1':
        return page1.layout
    elif pathname == '/':
        return page1.layout
    else:
        return '404'




if __name__ == '__main__':
    app.run_server(debug=False, port=8080)
