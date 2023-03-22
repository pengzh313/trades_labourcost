# import library
from dash import dash, html, dcc, dash_table, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

# read raw data
rates = pd.read_excel('../data/labour_rates.xlsx', sheet_name='rates')
shift = pd.read_excel('../data/labour_rates.xlsx', sheet_name='shift')
loa = pd.read_excel('../data/labour_rates.xlsx', sheet_name='LOA')

# data processing
# calculate weekly cost per person for all trades & shift combination
trade =[]
type_shift = []
cost_week = []

# all trades's weekly costs being calculated 
for t in ["BM", "MW", "IW", "PF"]:
    for s in ["5d_8h", "5d_10h", "6d_8h", "6d_10h"]:
        schedule = shift.query("trade==@t & type_shift==@s")
        rate = rates.query("trade==@t")
        cost_week_cal = round(((schedule.reset_index()["hr_weekday_st"][0]*
                          rate.query("type_time=='st'").reset_index()["rate_hourly"][0] +
                          schedule.reset_index()["hr_weekday_ot"][0]*
                          rate.query("type_time=='ot'").reset_index()["rate_hourly"][0])*5 +
                         (schedule.reset_index()["hr_sat_ot"][0]*
                          rate.query("type_time=='ot'").reset_index()["rate_hourly"][0] +
                          schedule.reset_index()["hr_sat_dt"][0]*
                          rate.query("type_time=='dt'").reset_index()["rate_hourly"][0])
                        ),2)
        trade.append(t)
        type_shift.append(s)
        cost_week.append(cost_week_cal)
hours_week = [40, 50, 48, 60, 40, 50, 48, 60, 40, 50, 48, 60, 40, 50, 48, 60]
df_cost_week = pd.DataFrame(list(zip(trade, type_shift, cost_week, hours_week)), 
                            columns = ["trade","type_shift","cost_week", "hours_week"])

# setup app and layout/frontend
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = "Trades Labour Costs Estimation"

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "5rem 1rem",
#    "background-color": "#ff6666",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [html.H2("Trades Weekly Labour Cost Estimation", className="display-10"),
     html.Hr(),
     html.P(
        "Select type of trades", style={"width": "100%"}
        ),
     dcc.RadioItems(id="trade_rad",
                    options=[{'label': 'Boilermaker', 'value': 'BM'},
                     {'label': 'Millwright', 'value': 'MW'},
                     {'label': 'Ironworker', 'value': 'IW'},
                     {'label': 'Pipefitter', 'value': 'PF'}       
                    ],
                    value='BM',
                    inline=False),
     html.Br(), #add vertical space 
     html.P(
        "Select type of shift ", style={"width": "100%"}
        ),              
     dcc.Dropdown(id="shift_drop",
                  options=["5d_8h",
                           "5d_10h",
                           "6d_8h",
                           "6d_10h"],
                  value="5d_8h",
                  placeholder="Select",
                  style={"width": "100%",
                         "color": "blue"}
                  )
    ],
    style=SIDEBAR_STYLE
)

content = dbc.Row([
    dbc.Card([dbc.Col([
                html.P("Comparison of weekly labour cost for different shift",
                       style={'text-align': 'center',
                              'font-weight': 'bold'}),
                dash_table.DataTable(
                    id='weekly_t_table',
                    columns=[{'name': i, 'id': i} for i in df_cost_week.columns],
                    data=df_cost_week.to_dict('records')
                )
    ])    
]),
    dbc.Card([dbc.Col(html.Br())]),
    dbc.Card([dbc.Col([
                html.P("Comparison of weekly labour cost for different trades",
                       style={'text-align': 'center',
                              'font-weight': 'bold'}),
                dash_table.DataTable(
                    id='weekly_s_table',
                    columns=[{'name': i, 'id': i} for i in df_cost_week.columns],
                    data=df_cost_week.to_dict('records')
                )
    ])    
]),
    dbc.Tab([
    html.Br(),
    "Note 1: BM - Boilermaker; MW - Millwright; IW - Ironworker; PF - Pipefitter",
    html.Br(),
    "Note 2: All cost in Canadian Dollars and for one tradesperson",
    html.Br(),
    "Note 3: Cost above for standard hourly wages only, allowances not included",
    html.Br(),
    "Note 4: Data is updated every May as per Union Collective Agreements"
    ])
],
    style=CONTENT_STYLE
)

app.layout = html.Div([sidebar, content])

@app.callback(
    Output('weekly_t_table', 'data'),
    Output('weekly_s_table', 'data'),
    Input('trade_rad', 'value'),
    Input('shift_drop', 'value')
)

def plot_cost_shift(trade_n, shift_n, df=df_cost_week.copy()):
    filter_trade = df.loc[(df['trade']==trade_n)]
    filter_shift = df.loc[(df['type_shift']==shift_n)]
    return filter_trade.to_dict('records'), filter_shift.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)