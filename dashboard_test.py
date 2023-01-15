import plotly.express as px
import pandas as pd
from datetime import date
import datetime
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import api
import dash_bootstrap_components as dbc



app = Dash(external_stylesheets=[dbc.themes.LUX])


#---------------------------------DASH CALLBACK---------------------------------


@app.callback(
    Output('graph', 'figure'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('dropdown', 'value'),
    prevent_initial_call=True)

def update_output(start_date, end_date, value):
    df = pd.DataFrame(api.get_data(start_date, end_date, value))
    fig = px.bar(df, x="time", y="price", barmode="group")
    return fig


#-----------------LAYOUT------------------------------------

app.layout = html.Div(children=[
    dbc.Row(
        dbc.Col(html.H1(children='Тестовое задание'), # TITLE
        width = 4,style = {'margin-left':'20px','margin-top':'7px'})),
    dbc.Row(    # Choose the coin
        dbc.Col(dcc.Dropdown(["bitcoin", "ethereum", "steem", "litecoin", "cardano", "tether", "dogecoin"], 
        value = "bitcoin", id ='dropdown'),
        width = 2,style = {'margin-left':'50px','margin-top':'20px'})),   
    dbc.Row([  # Date picker
        dbc.Col(dcc.DatePickerRange(
            id='my-date-picker-range',
            min_date_allowed=date(2019, 8, 5),
            initial_visible_month=datetime.datetime.now().date(),
            start_date=datetime.datetime.now().date(),
            end_date=datetime.datetime.now().date()),
            width = 3, style = {'margin-left':'50px', 'margin-top':'100px', 'margin-right':'15px'}),
        dbc.Col(dcc.Graph(id='graph'),  # GRAPH
        width = 8, style = {'margin-left':'15px', 'margin-top':'7px', 'margin-right':'15px'})])
])

if __name__ == '__main__':
    app.run_server(debug=True)