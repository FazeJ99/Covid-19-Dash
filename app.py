import pandas as pd  
import plotly          
import plotly.express as px

import dash             
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server
#---------------------------------------------------------------
#df = pd.read_csv("dataset\coviddata_cleaned.csv")
df = pd.read_csv("https://raw.githubusercontent.com/FazeJ99/Covid-19-Dash/refs/heads/main/dataset/coviddata_cleaned.csv")

dff = df.groupby('countriesAndTerritories', as_index=False)[['deaths','cases']].sum()
print (dff[:5])
#---------------------------------------------------------------
app.layout = html.Div( [html.H1("Covid-19 Analysis Dashboard", style={'text-align': 'center'}),
    html.Div([
        dash_table.DataTable(
            id='datatable_id',
            data=dff.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in dff.columns
            ],
            editable=False,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=False,
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 6,
            # page_action='none',
            # style_cell={
            # 'whiteSpace': 'normal'
            # },
            # fixed_rows={ 'headers': True, 'data': 0 },
            # virtualization=False,
            style_cell_conditional=[
                {'if': {'column_id': 'countriesAndTerritories'},
                 'width': '40%', 'textAlign': 'left'},
                {'if': {'column_id': 'deaths'},
                 'width': '30%', 'textAlign': 'left'},
                {'if': {'column_id': 'cases'},
                 'width': '30%', 'textAlign': 'left'},
            ],
        ),
    ],className='row'),

    html.Div([
        html.Div([
            dcc.Dropdown(id='linedropdown',
                options=[
                         {'label': 'Deaths', 'value': 'deaths'},
                         {'label': 'Cases', 'value': 'cases'}
                ],
                value='deaths',
                multi=False,
                clearable=False
            ),
        ],className='six columns'),

        html.Div([
        dcc.Dropdown(id='piedropdown',
            options=[
                     {'label': 'Deaths', 'value': 'deaths'},
                     {'label': 'Cases', 'value': 'cases'}
            ],
            value='cases',
            multi=False,
            clearable=False
        ),
        ],className='six columns'),

    ],className='row'),
    
     # Line and Bar Plots displayed side by side
     html.Div([
        html.Div([
            dcc.Graph(id='linechart', figure={})
        ], style={'width': '49%', 'display': 'inline-block'},className='sixcolumns'),

        html.Div([
            dcc.Graph(id='piechart', figure={})
        ], style={'width': '49%', 'display': 'inline-block'} , className='sixcolumns')
    ]),

])

#------------------------------------------------------------------
@app.callback(
    [Output('piechart', 'figure'),
     Output('linechart', 'figure')],
    [Input('datatable_id', 'selected_rows'),
     Input('piedropdown', 'value'),
     Input('linedropdown', 'value')]
)
def update_data(chosen_rows,piedropval,linedropval):
    if len(chosen_rows)==0:
        df_filterd = dff[dff['countriesAndTerritories'].isin(['China','Iran','Spain','Italy'])]
    else:
        print(chosen_rows)
        df_filterd = dff[dff.index.isin(chosen_rows)]

    pie_chart=px.pie(
            data_frame=df_filterd,
            names='countriesAndTerritories',
            values=piedropval,
            hole=.3,
            labels={'countriesAndTerritories':'Countries'},
            title='Pie Chart of Country Cases',
            )


    #extract list of chosen countries
    list_chosen_countries=df_filterd['countriesAndTerritories'].tolist()
    #filter original df according to chosen countries
    #because original df has all the complete dates
    df_line = df[df['countriesAndTerritories'].isin(list_chosen_countries)]

    line_chart = px.area(
            data_frame=df_line,
            x='dateRep',
            y=linedropval,
            color='countriesAndTerritories',
            labels={'countriesAndTerritories':'Countries', 'dateRep':'date'},
            title='Area Chart of Date against the country'
            )
    line_chart.update_layout(uirevision='foo')

    return (pie_chart,line_chart)

#------------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)