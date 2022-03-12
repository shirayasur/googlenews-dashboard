import dash
from dash import Dash, html, dcc, dash_table
from dash.dependencies import ClientsideFunction, Input, Output
from sqlalchemy import create_engine
import pymysql 

from news_dash_functions import *

from config import DB_CONNECTION_STRING

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
sqlEngine = create_engine(DB_CONNECTION_STRING, pool_recycle=3600)

def get_dbConnection():
    dbConnection = sqlEngine.connect()
    return dbConnection

pd.options.mode.chained_assignment = None

def generate_dropdown():
    dbc = get_dbConnection()
    return get_dropdown_names(dbc)

#Dashboard

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    
    html.Div(id='table-hidden-target', style={'display': 'none'}),

    
html.H1(children='In the News'),
    
    dcc.Markdown('Choose a keyword from the dropdown menu to see the news from this week.'),

        html.Div(children=[
            dcc.Dropdown(
        id='infra_news-dropdown',
        options=generate_dropdown(), 
        clearable = False,
        value = generate_dropdown()[0]['label']
    ),
    
        dash_table.DataTable(
    id='infra_table', 
    columns=[{'id': c, 'name': c} for c in ['Keyword', 'Title', 'Date', 'Link', 'Site']],
    style_cell={'textAlign': 'left',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 50,
        'whiteSpace': 'normal',
        'height': 'auto'},
            
    style_cell_conditional=[
        {
            'if': {'column_id': 'Keyword'},
            'width': '100px'
        },
        {
            'if': {'column_id': 'Date'},
            'width': '100px'
        },
        {
            'if': {'column_id': 'Title'},
            'width': '800px'
        },
         {
            'if': {'column_id': 'Link'},
            'width': '100px'
        },
        {
            'if': {'column_id': 'Site'},
            'width': '100px'
        },
    ],
    style_table={
        'overflowX': 'auto'
    },
                
        style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'}),
        ]),
        
        

])
#close app_layout


def generate_news_df():
    dbc = get_dbConnection()
    news_df = create_news_df(dbc)   
    return news_df


#Interactive Callbacks


@app.callback(
    dash.dependencies.Output('infra_table', 'data'),
    [dash.dependencies.Input('infra_news-dropdown', 'value')])
def update_news_output(value):
    #return generate_table(value)
    news_df = generate_news_df()
    news_comp_df = create_keyword_news(news_df, value)
    news_dict = news_comp_df.to_dict('records')
    return news_dict

app.clientside_callback(
    clientside_function = ClientsideFunction(namespace='ui',function_name='replaceWithLinks'),
    output = Output('table-hidden-target', 'children'),
    inputs=[Input('infra_table', 'derived_viewport_data')]
)



if __name__ == '__main__':
    app.run_server(port=8054,debug=True)
    





