import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd
import database
from sql_p import sql_ocupacao

dash.register_page(__name__, path="/",title='Ocupação Hospitalar')
external_css = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
]

layout = html.Div(
    children=[
        html.Div(
            [
                html.Img(src="/assets/logo_branca.png", className="logo"),
            ],
            className="cabecalho-navbar",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.A(href='1andar',children=[
                            dbc.Card(
                                [  
                                        dbc.CardBody(
                                            [
                                                html.H1(
                                                    "1º ANDAR",
                                                    className="text-center",
                                                    style={
                                                        "font-size": "25px",
                                                        "font-family": "Trebuchet MS",
                                                        "line-height": "1.0",
                                                    },
                                                ),
                                                html.Div(
                                                    id="total-ocupacao-1-andar",
                                                    className="text-center",
                                                    style={
                                                        "font-size": "30px",
                                                        "font-family": "Trebuchet MS",
                                                        "line-height": "2.0",
                                                    },
                                                ),
                                            ]
                                        )
                                    ],
                                    style={
                                        "width": "150px",
                                        "margin": "10px",
                                        "height": "130px",
                                        "color": "white",
                                        "background-color": "#104C70",
                                        
                                    },
                            )],style={"text-decoration": "none"}),
                        html.A(href='2leste',children=[
                            dbc.Card([
                                dbc.CardBody(
                                    [
                                        html.H1(
                                            "2º ANDAR",
                                            className="text-center",
                                            style={
                                                "font-size": "25px",
                                                "font-family": "Trebuchet MS",
                                                "line-height": "1.0",
                                            },
                                        ),
                                        html.Div(
                                            id="total-ocupacao-2-andar",
                                            className="text-center",
                                            style={
                                                "font-size": "30px",
                                                "font-family": "Trebuchet MS",
                                                "line-height": "2.0",
                                            },
                                        ),
                                    ]
                                )
                            ],
                            style={
                                "width": "150px",
                                "margin": "10px",
                                "height": "130px",
                                "color": "white",
                                "background-color": "#104C70",
                            },
                        )],style={"text-decoration": "none"}),
                        
                        html.A(href='3leste',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "3º LESTE",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-3-leste",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='3oeste',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "3º OESTE",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-3-oeste",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='4norte',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "4º ANDAR",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-4-andar",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='5norte',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "5º NORTE",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-5-norte",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='5sul',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "5º SUL",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-5-sul",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='6norte',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "6º NORTE",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-6-norte",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='6sul',children=[    
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "6º SUL",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-6-sul",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='7norte',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "7º NORTE",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-7-norte",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"}),
                        html.A(href='7sul',children=[
                            dbc.Card(
                                [
                                    dbc.CardBody(
                                        [
                                            html.H1(
                                                "7º SUL",
                                                className="text-center",
                                                style={
                                                    "font-size": "25px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "1.0",
                                                },
                                            ),
                                            html.Div(
                                                id="total-ocupacao-7-sul",
                                                className="text-center",
                                                style={
                                                    "font-size": "30px",
                                                    "font-family": "Trebuchet MS",
                                                    "line-height": "2.0",
                                                },
                                            ),
                                        ]
                                    )
                                ],
                                style={
                                    "width": "150px",
                                    "margin": "10px",
                                    "height": "130px",
                                    "color": "white",
                                    "background-color": "#104C70",
                                },
                            )],style={"text-decoration": "none"})
                    ],
                    style={
                        #"width": "80%",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "space-between",
                    },
                ),
                
            ],style={
                    #"width":'100%',
                    "display": "flex",
                    "justify-content": "center"
                    }
        ),
        dcc.Interval(
            id="interval-component-ocupacao",
            interval=30
            * 1000,  # Intervalo para atualização automática da página e dos dados
            n_intervals=0,  # Número inicial de intervalos
        ),
    ]
)


@callback(
    Output("total-ocupacao-1-andar", "children"),
    Output("total-ocupacao-2-andar", "children"),
    Output('total-ocupacao-3-leste', 'children'),
    Output('total-ocupacao-3-oeste', 'children'),
    Output('total-ocupacao-4-andar', 'children'),
    Output('total-ocupacao-5-norte', 'children'),
    Output('total-ocupacao-5-sul', 'children'),
    Output('total-ocupacao-6-norte', 'children'),
    Output('total-ocupacao-6-sul', 'children'),
    Output('total-ocupacao-7-norte', 'children'),
    Output('total-ocupacao-7-sul', 'children'),
    Input("interval-component-ocupacao", "n_intervals"),
)
def update_cards(n_intervals):
    df_ocupacao = database.get_data(sql_ocupacao)
    andar_1 = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 117]
    andar_2 = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 327]
    andar_3_leste = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 120]
    andar_3_oeste = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 118]
    andar_4 = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"]== 341]
    andar_5_norte = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 107]
    andar_5_sul = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 111]
    andar_6_norte = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 109]
    andar_6_sul = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 112]
    andar_7_norte = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 108]
    andar_7_sul = df_ocupacao[df_ocupacao["CD_SETOR_ATENDIMENTO"] == 110]


    qt_ocupacao_1andar = andar_1["PR_OCUPACAO"].sum()
    qt_ocupacao_2andar = andar_2["PR_OCUPACAO"].sum()
    qt_ocupacao_3_leste = andar_3_leste["PR_OCUPACAO"].sum()
    qt_ocupacao_3_oeste = andar_3_oeste["PR_OCUPACAO"].sum()
    qt_ocupacao_4andar = andar_4["PR_OCUPACAO"].sum()
    qt_ocupacao_5_norte = andar_5_norte["PR_OCUPACAO"].sum()
    qt_ocupacao_5_sul = andar_5_sul["PR_OCUPACAO"].sum()
    qt_ocupacao_6_norte = andar_6_norte["PR_OCUPACAO"].sum()
    qt_ocupacao_6_sul = andar_6_sul["PR_OCUPACAO"].sum()
    qt_ocupacao_7_norte = andar_7_norte["PR_OCUPACAO"].sum()
    qt_ocupacao_7_sul = andar_7_sul["PR_OCUPACAO"].sum()

    return f"{qt_ocupacao_1andar:.2f}%", f"{qt_ocupacao_2andar:.2f}%",f"{qt_ocupacao_3_leste:.2f}%",f"{qt_ocupacao_3_oeste:.2f}%",f"{qt_ocupacao_4andar:.2f}%",f"{qt_ocupacao_5_norte:.2f}%",f"{qt_ocupacao_5_sul:.2f}%",f"{qt_ocupacao_6_norte:.2f}%",f"{qt_ocupacao_6_sul:.2f}%",f"{qt_ocupacao_7_norte:.2f}%",f"{qt_ocupacao_7_sul:.2f}%"
