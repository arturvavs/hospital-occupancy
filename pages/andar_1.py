import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd
import database
from dash_iconify import DashIconify
from sql_p import sql

dash.register_page(__name__, path='/1andar',name='1º Andar')
layout = html.Div(children=[
    html.Div([
        html.Img(src='/assets/logo_branca.png', className='logo'),
        html.H1('UNIDADE DE INTERNAÇÃO', className='titulo'),
        html.H2('1º ANDAR', className='subtitulo')
    ],className='cabecalho'),
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    html.Div(children=[
#                                                                                               CARDS
        html.Div([
            dbc.Card([
                dbc.CardBody([
                    html.H1('Leitos', className='text-center', style={"font-size": "1.5625rem", "font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.Div(id='total-leitos-1andar', className='text-center', style={"font-size": "3.125rem", "font-family": "Trebuchet MS","line-height":"2.0"})
                ])], style={"width": "18.75rem", "margin": "0.625rem", "height": "11.25rem", "color": "white", "background-color": "#104C70"}),
        
            dbc.Card([
                dbc.CardBody([
                    html.H1('Pacientes',className='text-center', style={"font-size": "1.5625rem", "font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.Div(id='total-pacientes-1andar', className='text-center', style={"font-size": "3.125rem", "font-family": "Trebuchet MS","line-height":"2.0"})
                ])], style={"width": "18.75rem", "margin": "0.625rem", "height": "11.25rem", "color": "white", "background-color": "#007391"}),

            dbc.Card([
                dbc.CardBody([
                    html.H1('Livres',className='text-center', style={"font-size": "1.5625rem", "font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.Div(id='total-leitos-livres-1andar', className='text-center', style={"font-size": "3.125rem", "font-family": "Trebuchet MS","line-height":"2.0"})
                ])], style={"width": "18.75rem", "margin": "0.625rem", "height": "11.25rem", "color": "white", "background-color": "#4AA57D"}),

            dbc.Card([
                dbc.CardBody([
                    html.H1('Higienização',className='text-center', style={"font-size": "1.5625rem", "font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.Div(id='total-leitos-higienizacao-1andar', className='text-center', style={"font-size": "3.125rem", "font-family": "Trebuchet MS","line-height":"2.0"})
                ])], style={"width": "18.75rem", "margin": "0.625rem", "height": "11.25rem", "color": "white", "background-color": "#D13820"}),

            dbc.Card([
                dbc.CardBody([
                    html.H1('Reservados',className='text-center', style={"font-size": "1.5625rem", "font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.Div(id='total-leitos-reservados-1andar', className='text-center', style={"font-size": "3.125rem", "font-family": "Trebuchet MS","line-height":"2.0"})
                ])], style={"width": "18.75rem", "margin": "0.625rem", "height": "11.25rem", "color": "white", "background-color": "#FB5E3F"}),
        
            dbc.Card([
                dbc.CardHeader(
                    html.Div([
                        html.Img(src='/assets/patient-isolated.svg', style={'width': '1.875rem','height':'1.875rem', 'margin-right': '0.625rem'}),
                        html.Span('Precauções', style={"font-size": "1.5625rem", "font-family": "Trebuchet MS", "line-height": "1.0"})
                        ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
                        className='text-center', style={"background-color": "#104C70"}
                    ),
                dbc.CardBody([
                    html.Div([
                    html.H4('C - Contato', style={'margin-right': '0',"font-size":"1.0625rem","font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.H4('G - Gotículas', style={'margin-right': '0',"font-size":"1.0625rem","font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.H4('I - Imunossuprimidos', style={'margin-right': '0',"font-size":"1.0625rem","font-family": "Trebuchet MS","line-height":"1.0"}),
                    html.H4('GC - Gotículas e Contato', style={'margin-right': '0',"font-size":"1.0625rem","font-family": "Trebuchet MS","line-height":"1.0"})
                    ]),
                    html.Div([
                    html.H4('A - Aerossóis', style={'margin-right': '0',"font-size":"1.0625rem","font-family": "Trebuchet MS","line-height":"1.0"})    
                    ])   
                ],style={"font-size":"0.625rem","font-family": "Inter",'color':'black','display':'flex','flex-direction':'row','white-space':'nowrap'})
            ], style={"width": "26.875rem", "margin": "0.625rem", "height": "11.25rem", "color": "white", "background-color": "white", "font-size": "2.5rem", }),
        
        dbc.Card([
            dbc.CardHeader('MEOWS', className='text-center', style={"font-size": "1.5625rem","background-color": "#104C70","font-family": "Trebuchet MS","color": "white","line-height":"1.0"}),
            dbc.CardBody([
                html.Div([
                    html.Div([
                    html.Img(src='/assets/pontuacao_0.png', style={'width': '0.9375rem', 'margin-right': '0.625rem'}),
                    html.Span('Pontuação de 0-2', style={'margin-right': '0',"font-size":"0.9375rem",'fontWeight':'bold'})
                    ], style={'display': 'flex', 'align-items': 'center'}),
                html.Div([
                    html.Img(src='/assets/pontuacao_1.png', style={'width': '0.9375rem', 'margin-right': '0.625rem'}),
                    html.Span('Pontuação 3', style={'margin-right': '0',"font-size":"0.9375rem",'fontWeight':'bold'})
                    ], style={'display': 'flex', 'align-items': 'center'}),
                html.Div([
                    html.Img(src='/assets/pontuacao_2.png', style={'width': '0.9375rem', 'margin-right': '0.625rem'}),
                    html.Span('Pontuação de 4-5', style={'margin-right': '0',"font-size":"0.9375rem",'fontWeight':'bold'})
                    ], style={'display': 'flex', 'align-items': 'center'}),
                html.Div([
                    html.Img(src='/assets/pontuacao_3.png', style={'width': '0.9375rem', 'margin-right': '0.625rem'}),
                    html.Span('Pontuação >= 6', style={'margin-right': '0',"font-size":"0.9375rem",'fontWeight':'bold'})
                    ], style={'display': 'flex', 'align-items': 'center'}),
                ], style={'align-items': 'left','justify-content': 'space-between'})   
            ], style={"font-size":"0.625rem","font-family": "Trebuchet MS",'color':'black'})
        ], style={"width": "15.3125rem", "margin": "0.625rem", "height": "11.25rem", "color": "white", "background-color": "white", "font-size": "2.5rem"}),
    ], style={'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'space-between'})
    ]),
#TABELA
    html.Div([
        dash_table.DataTable(
        page_size=15, #Limite de linhas da página da tabela
        id='table-data-1andar',
        columns = [
            {'name': 'UNIDADE', 'id': 'CD_UNIDADE'},
            {'name': 'PACIENTE', 'id': 'NM_PESSOA_FISICA'},
            {'name': 'ALTA MÉD.', 'id': 'IE_RECOMEND_ALTA','presentation': 'markdown'},
            {'name': 'PRECAUÇÃO', 'id': 'DS_PRECAUCAO'},
            {'name': 'ATENDIMENTO', 'id': 'NR_ATENDIMENTO'},
            {'name': 'IDADE', 'id': 'NR_IDADE'},
            {'name': 'DIAS', 'id': 'QT_DIA_PERMANENCIA'},
            {'name': 'CLINICA', 'id': 'DS_CLINICA'},
            {'name': 'MED. RESPONSÁVEL', 'id': 'MEDICO'},
            {'name': 'CHAMADO TRR', 'id': 'COD_ACIONAMENTO','presentation':'markdown'},
            {'name': 'CONVÊNIO', 'id': 'DS_CONVENIO_ABREV'},
            {'name': 'DATA AVALIAÇÃO', 'id': 'DT_AVALIACAO'},
            {'name': 'MEOWS', 'id': 'QT_PONTUACAO_MOWS'},
            {'name': 'IE_STATUS_UNIDADE', 'id': 'IE_STATUS_UNIDADE'},
            {'name': 'SETOR_REDUZIDO', 'id': 'SETOR_REDUZIDO'},
            {'name': 'PENDENCIAS TRR', 'id':'QT_CHAMADOS_PENDENTES'}
            ],
        markdown_options={"html": True},
        hidden_columns=['IE_STATUS_UNIDADE','SETOR_REDUZIDO'],
        cell_selectable = False,
        style_table={
            #'border': '1px solid',
            'borderRadius': '10px',
            'overflow': 'hidden'
        },
        style_cell={
            'font-family': 'Trebuchet MS',
            'fontWeight': 'bold',
            'font_size': '18px',
            'text_align': 'center',
        },

        style_data_conditional=[
            {
                'if': {'column_id': ['NM_PESSOA_FISICA']},
                'textAlign': 'left',
                'whiteSpace': 'normal',
                'height': 'auto',
            },
            {
                'if': {'column_id': ['CD_UNIDADE']},
                'color':'white'
            },
            {
                'if': {'column_id': ['IE_RECOMEND_ALTA','CD_UNIDADE','NR_ATENDIMENTO','NR_IDADE','QT_DIA_PERMANENCIA','DS_CLINICA','MEDICO','DS_CONVENIO_ABREV','DT_AVALIACAO','QT_PONTUACAO_MOWS']},
                'textAlign': 'center',
                'whiteSpace': 'normal',
                'height': 'auto',
            },
            {
                'if': {
                    'filter_query':'{DS_PRECAUCAO} != " "',
                    'column_id':'NM_PESSOA_FISICA'
                },
                'backgroundColor':'#E1C233'
            },
            {
                'if': {
                    'filter_query':'{IE_STATUS_UNIDADE} = "P"', #COLUNA UNIDADE COM STATUS P = PACIENTE
                    'column_id':'CD_UNIDADE'
                },
                'backgroundColor':'#007391'
            },
            {
                'if': {
                    'filter_query':'{IE_STATUS_UNIDADE} = "L"',
                    'column_id':'CD_UNIDADE'
                },
                'backgroundColor':'#4aa57d'
            },
            {
                'if': {
                    'filter_query':'{IE_STATUS_UNIDADE} = "H"',
                    'column_id':'CD_UNIDADE'
                },
                'backgroundColor':'#D13820'
            },
            {
                'if': {
                    'filter_query':'{IE_STATUS_UNIDADE} = "R"',
                    'column_id':'CD_UNIDADE'
                },
                'backgroundColor':'#FB5E3F'
            },
            {
                'if': {
                    'filter_query':'{QT_PONTUACAO_MOWS} = "0" || {QT_PONTUACAO_MOWS} = "1" || {QT_PONTUACAO_MOWS} = "2"',
                    'column_id':'QT_PONTUACAO_MOWS'
                },
                'backgroundColor':'#41A4FF'
            },
            {
                'if': {
                    'filter_query':'{QT_PONTUACAO_MOWS} = "3"',
                    'column_id':'QT_PONTUACAO_MOWS'
                },
                'backgroundColor':'#1D8C01'
            },
            {
                'if': {
                    'filter_query':'{QT_PONTUACAO_MOWS} = "4" || {QT_PONTUACAO_MOWS} = "5"',
                    'column_id':'QT_PONTUACAO_MOWS'
                },
                'backgroundColor':'#FFFB00'
            },
            {
                'if': {
                    'filter_query':'{QT_PONTUACAO_MOWS} >= "6"',
                    'column_id':'QT_PONTUACAO_MOWS'
                },
                'backgroundColor':'#F60000'
            },   
            
        ],
        style_header={ #estilo do cabeçalho
            'font_family': 'Trebuchet MS',
            'font_size': '13px',
            'text_align': 'center',
            'fontWeight': 'bold',
            'backgroundColor': '#950707',
            'color': 'white'
            
        },
        fill_width=True,
        css=[{'selector':'.show-hide', 'rule': 'display : none'}]),#CSS QUE OCULTA O BOTÃO TOGGLE COLUMNS
        ],style={'width': '100%','padding':'10px'}),
    #dict(selector= "p", rule= "margin: 0; text-align: center")
    #{'selector':'.show-hide', 'rule': 'display : none'}
        dcc.Interval(
        id='interval-component-1andar',
        interval=30*1000,  # Intervalo para atualização automática da página e dos dados
        n_intervals=0  # Número inicial de intervalos
    ),
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#ARMAZENAMENTO DE INFORMAÇÃO SOBRE PAGINA DA TABELA
        dcc.Store(id='page-store-1andar', data={'current_page': 0}),
        dcc.Store(id='dataset-1andar'),

        html.Div([
        dcc.Link(href='1andar')
        ],className='link'),
        
       
],id='andar-1')

@callback(
    Output('total-leitos-1andar','children'),
    Output('total-pacientes-1andar','children'),
    Output('total-leitos-livres-1andar','children'),
    Output('total-leitos-higienizacao-1andar','children'),
    Output('total-leitos-reservados-1andar','children'),
    Output('dataset-1andar','data'),
    #Input('andar-1','id'),
    Input('interval-component-1andar', 'n_intervals')
)
def update_cards(n_invervals):#, n_intervals):
    df_pacientes = database.get_data(sql)
    src = '<i class="fa-solid fa-square-check" style="color: #2c9b39;"></i>'
    df_pacientes['IE_RECOMEND_ALTA'] = df_pacientes['IE_RECOMEND_ALTA'].apply(lambda x: src if x == 'SIM' else ' ')
    filter_df_pacientes = df_pacientes
    setor = '1º ANDAR'
    filter_df_pacientes = filter_df_pacientes[filter_df_pacientes['SETOR_REDUZIDO'] == setor]
    #src = '/assets/check-icone-3.png'
    qt_leitos = len(filter_df_pacientes)
    qt_pacientes = filter_df_pacientes[(filter_df_pacientes['IE_STATUS_UNIDADE']== 'P')].shape[0]
    qt_leitos_livres = filter_df_pacientes[(filter_df_pacientes['IE_STATUS_UNIDADE']== 'L')].shape[0]
    qt_leitos_higienizacao = filter_df_pacientes[(filter_df_pacientes['IE_STATUS_UNIDADE']== 'H')].shape[0]
    qt_leitos_reservados = filter_df_pacientes[(filter_df_pacientes['IE_STATUS_UNIDADE']== 'R')].shape[0]
    return qt_leitos,qt_pacientes,qt_leitos_livres,qt_leitos_higienizacao,qt_leitos_reservados,df_pacientes.to_json(date_format='iso', orient='split')

@callback(
    Output('table-data-1andar', 'data'), #Callback para atualizar a tabela
    Output('table-data-1andar', 'page_current'), #Callback para atualizar a página da tabela
    Input('interval-component-1andar', 'n_intervals'), #Callback que obtem do dcc.Interval o valor n_intervals para atualização da página
    Input('dataset-1andar','data'),
    #Input('andar-1','id'),
    State('page-store-1andar', 'data') #Callback para identificar qual a página atual da tabela
)
def update_table(n_intervals,jsonified_cleaned_data, page_store):
    def condition(x):
        if x == 'Vermelho (Alto Risco)':
            src_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 72 72"><circle cx="36" cy="36" r="28" fill="#d22f27"/><circle cx="36" cy="36" r="28" fill="none" stroke="#000" stroke-linejoin="round" stroke-width="2"/></svg>'
        elif x == 'Amarelo (Médio Risco)':
            src_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 72 72"><circle cx="36" cy="36" r="28" fill="#f3e22b"/><circle cx="36" cy="36" r="28" fill="none" stroke="#000" stroke-linejoin="round" stroke-width="2"/></svg>'
        elif x == 'Verde (Baixo Risco)':
            src_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 72 72"><circle cx="36" cy="36" r="28" fill="#2bf342"/><circle cx="36" cy="36" r="28" fill="none" stroke="#000" stroke-linejoin="round" stroke-width="2"/></svg>'
        elif x == 'Azul (Baixo Risco)':
            src_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 72 72"><circle cx="36" cy="36" r="28" fill="#3227d3"/><circle cx="36" cy="36" r="28" fill="none" stroke="#000" stroke-linejoin="round" stroke-width="2"/></svg>'
        elif x == 'Branco (Sem risco)':
            src_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 72 72"><circle cx="36" cy="36" r="28" fill="#FFFFFF"/><circle cx="36" cy="36" r="28" fill="none" stroke="#000" stroke-linejoin="round" stroke-width="2"/></svg>'
        elif x == 'Laranja (Admissão)':
            src_icon = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 72 72"><circle cx="36" cy="36" r="28" fill="#ffa200"/><circle cx="36" cy="36" r="28" fill="none" stroke="#000" stroke-linejoin="round" stroke-width="2"/></svg>'
        else:
            src_icon = ' '
        return src_icon
    df_pacientes = pd.read_json(jsonified_cleaned_data,orient='split')  # Obter os dados mais recentes
    #df_pacientes = database.global_data
    filtered_df_pacientes = df_pacientes
    filtered_df_pacientes.loc[:, 'COD_ACIONAMENTO'] = filtered_df_pacientes['COD_ACIONAMENTO'].astype('object')
    setor = '1º ANDAR'
    filtered_df_pacientes = filtered_df_pacientes[filtered_df_pacientes['SETOR_REDUZIDO'] == setor]
    filtered_df_pacientes.loc[:, 'COD_ACIONAMENTO'] = filtered_df_pacientes['COD_ACIONAMENTO'].apply(condition)
    total_pages = (len(filtered_df_pacientes) + 14) // 15  # Calcular o número total de páginas
    current_page = page_store['current_page']
    current_page = (current_page + 1) % total_pages  # Atualizar a página atual
    return filtered_df_pacientes.to_dict('records'), current_page
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#CALLBACK DA ATUALIZAÇÃO E PAGINAÇÃO DA TABELA
@callback(
    Output('page-store-1andar', 'data'),
    Input('interval-component-1andar', 'n_intervals'),
    State('page-store-1andar', 'data')
)
def update_page_store(n_intervals, page_store):
    total_pages = 10  # Numero total de páginas que a tabela terá
    current_page = page_store['current_page']
    current_page = (current_page + 1) % total_pages  # Incrementar a página atual
    return {'current_page': current_page}