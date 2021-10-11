import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import math



FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
app = dash.Dash(__name__, external_stylesheets=[
                dbc.themes.BOOTSTRAP, FONT_AWESOME])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand(
                        "Mobility Optimizers", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plotly.com",
        ),
        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
    ],
    color="dark",
    dark=True,
)


app.layout = html.Div([
    navbar,
    dbc.Container([
        dbc.Row(
            dbc.Col([
                html.Div([
                    dcc.Graph(
                        id='gauge-chart'
                    ),

                    html.Hr()
                ],style={'textAlign': 'center'}
                ),
                dbc.Card([
                    dcc.Slider(
                        id='my-slider',
                        min=0,
                        max=100000,
                        step=10000,
                        value=50000,
                        marks={i: {'label': str(int(i/1000))+'k'}
                            for i in range(0, 100000+10000, 10000)}
                    ),
                    html.Span(["Number of Cars Per Day ",
                            html.I(className="fas fa-question-circle fa-sm",
                                    id="target"),
                            dbc.Popover([
                                dbc.PopoverHeader('Header'),
                                dbc.PopoverBody(
                                    "And here's some amazing content. Cool!"),
                            ], target="target", trigger="legacy",
                            ),
                            ], style={'textAlign': 'center'})
                ])
            ], lg=6,
            ), justify="center", align="center",  # style={"height": "55vh"}
        )
    ], fluid=True)

])



@app.callback(
    dash.dependencies.Output('gauge-chart', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    val = value * (22/25.7) * 8887/1000000000
    print(val)
    return go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = val,
    mode = "gauge+number+delta",
    title = {'text': "Predicted Ground-Level Ozone Concentration (PPM)"},
    delta = {'reference': 0.7, 'increasing.color':'red', 'decreasing.color':'green'},
    gauge = {'axis': {'range': [None, 1]},
             'steps' : [
                 {'range': [0, 1], 'color':'white'}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': .7}}))

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)