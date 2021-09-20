import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
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
                    html.H1(
                        className="card-text", id='slider-output-container', style={'textAlign': 'center'}
                    ),
                    html.H6("Ground Level Ozone Emissions (Metric Tons)",
                            className="card-text",  style={'textAlign': 'center'}
                            ),
                    html.Hr()
                ]
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
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return "{:,}".format(math.floor(value * (22/25.7) * 8887/1000000))


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)