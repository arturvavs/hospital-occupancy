sql = """
select
    a.cd_setor_atendimento,
    obter_nome_setor(a.cd_setor_atendimento) setor,
    substr(obter_nome_setor(a.cd_setor_atendimento), 23)setor_reduzido,
    a.cd_unidade,
    c.ie_status_unidade,
    a.nr_atendimento,
    a.nr_prontuario,
    a.cd_pessoa_fisica,
    a.nm_pessoa_fisica,
    a.ds_convenio,
    nvl(substr(a.ds_convenio,1,instr(a.ds_convenio, ' - ',1)), substr(a.ds_convenio,1,50)) ds_convenio_abrev,
    decode(a.nm_guerra, null, '', 'DR. ' || obter_nome_sobrenome_pessoa(obter_dados_atendimento(a.nr_atendimento, 'MR'), 'P') || ' ' ||obter_nome_sobrenome_pessoa(obter_dados_atendimento(a.nr_atendimento, 'MR'), 'S')) medico,
    a.qt_dia_permanencia,
    a.ds_clinica,
    obter_dados_pf(a.cd_pessoa_fisica, 'I') nr_idade,
    obter_faixa_etaria_censo(a.cd_pessoa_fisica) faixa_etaria,
    a.ie_sexo_paciente,
    obter_iniciais_nome(null,nm_pessoa_fisica) iniciais,
    decode(a.ie_sexo_paciente,'f',1,'m',2) ie_sexo,
        (
        select
            max(pm.dt_prescricao)
        from
            prescr_medica pm
        where
            1 = 1
            and pm.dt_liberacao is not null
            and pm.nr_atendimento = a.nr_atendimento
            and pm.dt_suspensao is null
            and pm.ie_funcao_prescritor = 1
    ) data_presc, 
     (select  (qt_pontuacao)
           from     escala_mews e  
           where    e.nr_sequencia =   (select   max(e.nr_sequencia)
                                     from     escala_mews e
                                     where     e.nr_atendimento = a.nr_atendimento
                                     and ie_situacao ='A'))qt_pontuacao,
    (select   
    qt_pontos
        from     escala_eif_ii e  
           where    e.nr_sequencia =   (select   max(e.nr_sequencia)
                                     from     escala_eif_ii e
                                     where     e.nr_atendimento = a.nr_atendimento
                                     and e.nr_seq_escala in (1,12)
                                     and ie_situacao ='A'))qt_pontuacao_mows,
    to_char((select
            dt_avaliacao
        from
            escala_mews e
        where
            e.nr_sequencia = (
                select
                    max(e.nr_sequencia)
                from
                    escala_mews e
                where
                        e.nr_atendimento = a.nr_atendimento
                    and ie_situacao = 'A')),'dd/mm hh24:mi') dt_avaliacao,
                    nvl(HCD_OBTER_INICIAIS_PRECAUCAO(a.nr_atendimento),' ') ds_precaucao,
    case when exists (select 1 from cpoe_recomendacao x where x.nr_atendimento = a.nr_atendimento and x.cd_recomendacao in (179,289)) then 'SIM'
    else '' end IE_RECOMEND_ALTA,
    case when exists (select 1 from ehr_registro x where x.nr_seq_templ = 100777 and x.dt_liberacao is not null and x.dt_inativacao is null and x.nr_atendimento = a.nr_atendimento) then (select 
    count(*)qt_chamados
    from ATENDIMENTO_PACIENTE i, ehr_registro j, ehr_reg_template l
    where 1=1
    and i.nr_atendimento = j.nr_atendimento
    and j.nr_sequencia = l.nr_seq_reg
    and l.nr_seq_template = 100776
    and j.dt_inativacao is null
    and j.dt_liberacao is not null
    and not exists (select 1 from ehr_reg_template x, ehr_reg_elemento y, ehr_registro z
                    where x.nr_sequencia = y.nr_seq_reg_template
                    and x.nr_seq_reg = z.nr_sequencia
                    and z.nr_atendimento  = i.nr_atendimento
                    and y.nr_seq_temp_conteudo = 291501
                    and x.nr_seq_template = 100777
                    and x.dt_inativacao is null
                    and y.ds_resultado = ehr_vlr(l.nr_sequencia,291517,null,null) 
                    and x.dt_liberacao is not null
                    )
    and ehr_vlr(l.nr_sequencia,291489,null,null) is not null
    and j.dt_liberacao > (select max(k.dt_liberacao) from ehr_registro k where k.nr_atendimento = j.nr_atendimento and k.nr_seq_templ = 100777)
    and i.nr_atendimento = a.nr_atendimento)
    else (select count(*) from ehr_registro x where x.nr_seq_templ = 100776 and x.dt_liberacao is not null and x.dt_inativacao is null and x.nr_atendimento = a.nr_atendimento) end QT_CHAMADOS_PENDENTES,
    hcd_get_code_trr_call(a.nr_atendimento)cod_acionamento
    
    
    
from
    ocupacao_unidade_v   a, setor_atendimento_v b, unidade_atendimento c
where 1=1
and a.cd_setor_atendimento = b.cd_setor_atendimento
and a.cd_setor_atendimento = c.cd_setor_atendimento
and a.cd_unidade_basica = c.cd_unidade_basica
and a.cd_unidade_compl = c.cd_unidade_compl
and c.ie_situacao = 'A'
and b.cd_setor_atendimento in (117,327,120,118,341,107,111,109,112,108,110)
and c.ie_status_unidade in ('H', 'L', 'P', 'R')
and c.cd_tipo_acomodacao not in ( 2 )
order by a.cd_unidade
"""

sql_co = """SELECT 
    (a.cd_unidade_basica || ' ' || a.cd_unidade_compl) cd_unidade,
    b.nr_atendimento,
    substr(Obter_Nome_PF_Oculta(b.cd_pessoa_fisica,1848,'ARTUR.VINICIUS'),1,255) nm_pessoa_fisica,
    substr(Obter_Idade_PF(b.cd_pessoa_fisica, sysdate, 'S'),1,100) ds_idade,
    substr(obter_nome_medico(b.cd_medico_resp,'G'),1,255) nm_guerra,
    substr(obter_desc_cid(obter_cid_atendimento(b.nr_atendimento,'P')),1,240) ds_diagnostico,
    (select x.qt_sem_ig_ini_pre_natal from parto x where x.nr_atendimento = b.nr_atendimento and x.nr_sequencia = (select max(z.nr_sequencia) from parto z where z.nr_atendimento = x.nr_atendimento and z.dt_liberacao is not null and z.dt_inativacao is null))IG_Inicio_Semanas,
    (select x.qt_sem_ig_ecografica from parto x where x.nr_atendimento = b.nr_atendimento and x.nr_sequencia = (select max(z.nr_sequencia) from parto z where z.nr_atendimento = x.nr_atendimento and z.dt_liberacao is not null and z.dt_inativacao is null))IG_US_Semanas
FROM	 setor_atendimento s,
	 atend_paciente_unidade a,
	 atendimento_paciente b
WHERE ('CC' = 'CC') 
 
	AND	a.cd_setor_atendimento = s.cd_setor_atendimento
	AND	b.nr_atendimento = a.nr_atendimento 
	AND	a.cd_setor_atendimento = 208 
	AND	a.dt_saida_unidade is null 
	AND	a.dt_entrada_unidade > sysdate - 10 
	AND	substr(Obter_se_enfermeiro_resp(a.nr_atendimento,'1169498','T'),1,1) = 'S'
ORDER BY somente_numero(a.cd_unidade_basica) ,
	 nm_pessoa_fisica 
"""
sql_ocupacao = """SELECT 
       CD_SETOR_ATENDIMENTO,
       DS_SETOR_ATENDIMENTO,
      round(DECODE((NR_UNIDADES_SETOR - NR_UNIDADES_TEMPORARIAS),0, 0,
      (NR_UNIDADES_OCUPADAS * 100 / (NR_UNIDADES_SETOR -
              NR_UNIDADES_TEMPORARIAS + NR_UNID_TEMP_OCUP))),2) PR_OCUPACAO
FROM   HCD_OCUPACAO_SETORES_V
where  ie_ocup_hospitalar = 'S'
and cd_setor_atendimento not in (320)
 """