import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State
import dash_bootstrap_components as dbc
import pandas as pd
import database
from sql_p import sql_co

# Registra a página com o Dash
dash.register_page(__name__, path='/co',name='Centro Obstétrico')

# Define o layout da página
layout = html.Div(children=[
    html.Div([
        
        html.A(href='/',style={'width':'12%','display':'block','margin':'0.3125rem 0rem','margin-left':'0.3125rem'}, children=[
            html.Img(src='/assets/logo_branca.png',style={'width':'100%'})]),
        html.H1('CENTRO OBSTÉTRICO', className='titulo'),
        html.H2(' ', className='subtitulo')
    ], className='cabecalho'),

    html.Div([
        dash_table.DataTable(
            page_size=15, # Limite de linhas da página da tabela
            id='table-data-co',
            columns=[
                {'name': 'UNIDADE', 'id': 'CD_UNIDADE'},
                {'name': 'PACIENTE', 'id': 'NM_PESSOA_FISICA'},
                {'name': 'ATENDIMENTO', 'id': 'NR_ATENDIMENTO'},
                {'name': 'DIAGNOSTICO', 'id': 'DS_DIAGNOSTICO'},
                {'name': 'IG (Semanas)', 'id': 'IG_INICIO_SEMANAS'},
                {'name': 'IG US (Semanas)', 'id': 'IG_US_SEMANAS'}
            ],
            style_table={
                'borderRadius': '10px',
                'overflow': 'hidden'
            },
            style_cell={
                'font-family': 'Trebuchet MS',
                'fontWeight': 'bold',
                'font_size': '18px',
                'text_align': 'center',
            },
            style_header={
                'font_family': 'Trebuchet MS',
                'font_size': '13px',
                'text_align': 'center',
                'fontWeight': 'bold',
                'backgroundColor': '#950707',
                'color': 'white'
            },
            style_data_conditional=[
            {
                'if': {'column_id': ['NM_PESSOA_FISICA','DS_DIAGNOSTICO']},
                'textAlign': 'center',
                'whiteSpace': 'normal',
                'height': 'auto',
            },],
            fill_width=True,
            css=[{'selector': '.show-hide', 'rule': 'display : none'}], # CSS para ocultar o botão de alternar colunas
            page_current=0  # Adiciona controle manual da página
        ),
    ], style={'width': '100%', 'padding': '10px'}),

    dcc.Interval(
        id='interval-component-co',
        interval=30*1000,  # Intervalo para atualização automática da página e dos dados
        n_intervals=0  # Número inicial de intervalos
    ),

    dcc.Store(id='page-store-co', data={'current_page': 0}),
    
    html.Div([
        dcc.Link(href='/co')
    ], className='link')
], id='layout_co')


@callback(
    Output('table-data-co', 'data'),  # Callback para atualizar a tabela
    Output('table-data-co', 'page_current'),  # Callback para atualizar a página da tabela
    Input('interval-component-co', 'n_intervals'),  # Valor n_intervals para atualização
    State('page-store-co', 'data')  # Identificar qual a página atual da tabela
)
def update_table(n_intervals, page_store):
    df_pacientes = database.get_data(sql_co)  # Obter os dados mais recentes
    if df_pacientes.empty:
        return [], 0
    
    total_pages = (len(df_pacientes) + 14) // 15  # Calcular o número total de páginas
    current_page = page_store['current_page']
    current_page = (current_page + 1) % total_pages  # Atualizar a página atual

    # Paginar os dados manualmente
    start = current_page * 15
    end = start + 15
    page_data = df_pacientes.iloc[start:end].to_dict('records')
    return page_data, current_page


@callback(
    Output('page-store-co', 'data'),
    Input('interval-component-co', 'n_intervals'),
    State('page-store-co', 'data')
)
def update_page_store(n_intervals, page_store):
    total_pages = 10  # Número total de páginas
    current_page = page_store['current_page']
    current_page = (current_page + 1) % total_pages  # Incrementar a página atual
    return {'current_page': current_page}
