import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
covid_data = pd.read_csv(r"C:\Users\sathy\OneDrive\Documents\COVID19_Dashboard\covid_cleaned.csv")
covid_data['date'] = pd.to_datetime(covid_data['date'], errors='coerce')
app = Dash(__name__)
app.title = "🌍 COVID-19 Analytics Dashboard"
countries = sorted(covid_data['country'].unique())
app.layout = html.Div([
    html.H1("🌍 Global COVID-19 Dashboard", style={'textAlign': 'center', 'color': '#004aad'}),

    html.Div([
        html.Label("Select Country:", style={'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': c, 'value': c} for c in countries],
            value='India',
            style={'width': '60%', 'margin': 'auto'}
        )
    ], style={'textAlign': 'center', 'padding': '20px'}),

    html.Div(id='summary-cards', style={
        'display': 'flex',
        'justifyContent': 'center',
        'gap': '30px',
        'marginTop': '20px'
    }),

    html.Div([
        dcc.Graph(id='cases-graph'),
        dcc.Graph(id='deaths-graph')
    ])
])
@app.callback(
    [Output('cases-graph', 'figure'),
     Output('deaths-graph', 'figure'),
     Output('summary-cards', 'children')],
    [Input('country-dropdown', 'value')]
)
def update_dashboard(selected_country):
    filtered = covid_data[covid_data['country'] == selected_country]


    fig_cases = px.line(
        filtered, x='date', y='cumulative_total_cases',
        title=f'Cumulative Cases in {selected_country}',
        color_discrete_sequence=['#007bff']
    )

    fig_deaths = px.line(
        filtered, x='date', y='cumulative_total_deaths',
        title=f'Cumulative Deaths in {selected_country}',
        color_discrete_sequence=['#ff4d4d']
    )

    fig_cases.update_layout(xaxis_title="Date", yaxis_title="Cases", template='plotly_white')
    fig_deaths.update_layout(xaxis_title="Date", yaxis_title="Deaths", template='plotly_white')

    # Summary Cards
    latest_data = filtered.sort_values('date').iloc[-1]
    cards = [
        html.Div([
            html.H3(f"{int(latest_data['cumulative_total_cases']):,}", style={'color': '#007bff'}),
            html.P("Total Cases", style={'fontWeight': 'bold'})
        ], style={'padding': '15px', 'border': '2px solid #007bff', 'borderRadius': '10px', 'width': '200px', 'textAlign': 'center'}),

        html.Div([
            html.H3(f"{int(latest_data['cumulative_total_deaths']):,}", style={'color': '#ff4d4d'}),
            html.P("Total Deaths", style={'fontWeight': 'bold'})
        ], style={'padding': '15px', 'border': '2px solid #ff4d4d', 'borderRadius': '10px', 'width': '200px', 'textAlign': 'center'}),

        html.Div([
            html.H3(f"{int(latest_data['active_cases']):,}", style={'color': '#ffa500'}),
            html.P("Active Cases", style={'fontWeight': 'bold'})
        ], style={'padding': '15px', 'border': '2px solid #ffa500', 'borderRadius': '10px', 'width': '200px', 'textAlign': 'center'})
    ]

    return fig_cases, fig_deaths, cards

if __name__ == '__main__':
    app.run(debug=True)