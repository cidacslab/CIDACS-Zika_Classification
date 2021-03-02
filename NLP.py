# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:03:47 2021

@author: rafae
"""
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
import unidecode
import numpy as np
from spacy.tokens import Token
import html
import re
import pickle as pk

class NLP:
    def __init__(self):
        self.nlp = spacy.load("pt_core_news_lg")
        stopPalavras = list(STOP_WORDS)
        stopPalavras.append("06h")
        stopPalavras.append("07h")
        stopPalavras.append("0a")
        stopPalavras.append("10dias")
        stopPalavras.append("10ui")
        stopPalavras.append("110x70")
        stopPalavras.append("12d")
        stopPalavras.append("12s")
        stopPalavras.append("13s")
        stopPalavras.append("14sm")
        stopPalavras.append("15sm")
        stopPalavras.append("17h")
        stopPalavras.append("18s")
        stopPalavras.append("1dia")
        stopPalavras.append("1gg")
        stopPalavras.append("1gm")
        stopPalavras.append("1odose")
        stopPalavras.append("1ot")
        stopPalavras.append("200ui")
        stopPalavras.append("200x190")
        stopPalavras.append("20150vdrl")
        stopPalavras.append("20mcg")
        stopPalavras.append("20s")
        stopPalavras.append("20s6d")
        stopPalavras.append("21dp")
        stopPalavras.append("21sm")
        stopPalavras.append("22s")
        stopPalavras.append("23s")
        stopPalavras.append("23sm")
        stopPalavras.append("24h")
        stopPalavras.append("25s")
        stopPalavras.append("26semanas")
        stopPalavras.append("28sem")
        stopPalavras.append("2d")
        stopPalavras.append("2dp")
        stopPalavras.append("2sm")
        stopPalavras.append("2tri")
        stopPalavras.append("30s")
        stopPalavras.append("31s")
        stopPalavras.append("33sem")
        stopPalavras.append("34s")
        stopPalavras.append("36s")
        stopPalavras.append("36s3d")
        stopPalavras.append("36sm")
        stopPalavras.append("37s1d")
        stopPalavras.append("37s2d")
        stopPalavras.append("37s5d")
        stopPalavras.append("38oc")
        stopPalavras.append("38s1d")
        stopPalavras.append("38s")
        stopPalavras.append("38sem")
        stopPalavras.append("38semanas")
        stopPalavras.append("39sm")
        stopPalavras.append("39s")
        stopPalavras.append("38s")
        stopPalavras.append("3omes")
        stopPalavras.append("3tri")
        stopPalavras.append("48h")
        stopPalavras.append("4sm")
        stopPalavras.append("51ui")
        stopPalavras.append("5ag")
        stopPalavras.append("6consultas")
        stopPalavras.append("6d")
        stopPalavras.append("9797ba")
        stopPalavras.append("a0")
        stopPalavras.append("aas")
        stopPalavras.append("ab")
        stopPalavras.append("abar")
        stopPalavras.append("abd")
        stopPalavras.append("abril")
        stopPalavras.append("absag")
        stopPalavras.append("ac")
        stopPalavras.append("achar")
        stopPalavras.append("acirc")
        stopPalavras.append("acm")
        stopPalavras.append("acolhido")
        stopPalavras.append("acolhimento")
        stopPalavras.append("acometer")
        stopPalavras.append("acompanhamento")
        stopPalavras.append("acompanhante")
        stopPalavras.append("acompanhar")
        stopPalavras.append("adequadamente")
        stopPalavras.append("adm")
        stopPalavras.append("adm")
        stopPalavras.append("admissao")
        stopPalavras.append("admissional")
        stopPalavras.append("admitir")
        stopPalavras.append("aceito")
        stopPalavras.append("adequar")
        stopPalavras.append("adicionar")
        stopPalavras.append("administrar")
        stopPalavras.append("adquirir")
        stopPalavras.append("af")
        stopPalavras.append("afirmar")
        stopPalavras.append("ag")
        stopPalavras.append("agendar")
        stopPalavras.append("agente")
        stopPalavras.append("aghabs")
        stopPalavras.append("aguardar")
        stopPalavras.append("aig")
        stopPalavras.append("aina")
        stopPalavras.append("a1")
        stopPalavras.append("alagoinhas")
        stopPalavras.append("albert")
        stopPalavras.append('align"justify')
        stopPalavras.append('alves')
        stopPalavras.append('am')
        stopPalavras.append('ambigua')
        stopPalavras.append('amostrar')
        stopPalavras.append('analisar')
        stopPalavras.append('andamento')
        stopPalavras.append('anit')
        stopPalavras.append('ano')
        stopPalavras.append('anotacao')
        stopPalavras.append('aometodo')
        stopPalavras.append('ap')
        stopPalavras.append('aparentar')
        stopPalavras.append('apo')
        stopPalavras.append('apr')
        stopPalavras.append('aprese')
        stopPalavras.append('aproximadamente')
        stopPalavras.append('arlinda')
        stopPalavras.append('ass')
        stopPalavras.append('at')
        stopPalavras.append('assistencia')
        stopPalavras.append('assistente')
        stopPalavras.append('atar')
        stopPalavras.append('atb')
        stopPalavras.append('atendido')
        stopPalavras.append('atendimento')
        stopPalavras.append('ater')
        stopPalavras.append('atrasar')
        stopPalavras.append('atravez')
        stopPalavras.append('atualizacao')
        stopPalavras.append('atualizado')
        stopPalavras.append('aume')
        stopPalavras.append('aus')
        stopPalavras.append('ausentar')
        stopPalavras.append('automedicacao')
        stopPalavras.append('av')
        stopPalavras.append('avaliar')
        stopPalavras.append('b')
        stopPalavras.append('bebr')
        stopPalavras.append('born')
        stopPalavras.append('bo')
        stopPalavras.append('br')
        stopPalavras.append('buscar')
        stopPalavras.append('ca27')
        stopPalavras.append('ca28')
        stopPalavras.append('caber')
        stopPalavras.append('caetano')
        stopPalavras.append('caf')
        stopPalavras.append('camacari')
        stopPalavras.append('capibarib')
        stopPalavras.append('captar')
        stopPalavras.append('caracterizar')
        stopPalavras.append('caratcerizada')
        stopPalavras.append('caribe')
        stopPalavras.append('carlos')
        stopPalavras.append('cartao')
        stopPalavras.append('carteiro')
        stopPalavras.append('casar')
        stopPalavras.append('caso')
        stopPalavras.append('causar')
        stopPalavras.append('chegar')
        stopPalavras.append('chorar')
        stopPalavras.append('cid')
        stopPalavras.append('cidade')
        stopPalavras.append('cigarro')
        stopPalavras.append('citar')
        stopPalavras.append('civil')
        stopPalavras.append('clareza')
        stopPalavras.append('classificacao')
        stopPalavras.append('classificar')
        stopPalavras.append('clinicamente')
        stopPalavras.append('clinicar')
        stopPalavras.append('clinico')
        stopPalavras.append('coeficiente')
        stopPalavras.append('coleta')
        stopPalavras.append('coletadas')
        stopPalavras.append('coletado')
        stopPalavras.append('coletados')
        stopPalavras.append('coletou')
        stopPalavras.append('colher')
        stopPalavras.append('colhido')
        stopPalavras.append('comentario')
        stopPalavras.append('comer')
        stopPalavras.append('comp')
        stopPalavras.append('companheiro')
        stopPalavras.append('comparecer')
        stopPalavras.append('compensatoria')
        stopPalavras.append('compensatorio')
        stopPalavras.append('comprimento')
        stopPalavras.append('computar')
        stopPalavras.append('conhecer')
        stopPalavras.append('conjugal')
        stopPalavras.append('conjuge')
        stopPalavras.append('conseguir')
        stopPalavras.append('consumir')
        stopPalavras.append('contar')
        stopPalavras.append('continuar')
        stopPalavras.append('correspondente')
        stopPalavras.append('descobrir')
        stopPalavras.append('descrever')
        stopPalavras.append('descrito')
        stopPalavras.append('devidamente')
        stopPalavras.append('dia018')
        stopPalavras.append('dia16')
        stopPalavras.append('diariamente')
        stopPalavras.append('dimens')
        stopPalavras.append('dimensao')
        stopPalavras.append('dirigir')
        stopPalavras.append('div')
        stopPalavras.append('documento')
        stopPalavras.append('dosar')
        stopPalavras.append('dose')
        stopPalavras.append('doutor')
        stopPalavras.append('dr')
        stopPalavras.append('duarte')
        stopPalavras.append('durar')
        stopPalavras.append('duvidar')
        stopPalavras.append('efeito')
        stopPalavras.append('elisa')
        stopPalavras.append('email')
        stopPalavras.append('encaminh')
        stopPalavras.append('encaminhamento')
        stopPalavras.append('encaminhar')
        stopPalavras.append('enfermeiro')
        stopPalavras.append('engravidar')
        stopPalavras.append('ensinar')
        stopPalavras.append('entanto')
        stopPalavras.append('enviar')
        stopPalavras.append('episodio')
        stopPalavras.append('epoca')
        stopPalavras.append('equipar')
        stopPalavras.append('escolaridade')
        stopPalavras.append('espacar')
        stopPalavras.append('especialmente')
        stopPalavras.append('especificar')
        stopPalavras.append('esperar')
        stopPalavras.append('esquema')
        stopPalavras.append('estudo')
        stopPalavras.append('etc')
        stopPalavras.append('eunapolis')
        stopPalavras.append('exam')
        stopPalavras.append('expediente')
        stopPalavras.append('favorecer')
        stopPalavras.append('fem')
        stopPalavras.append('feminino')
        stopPalavras.append('ficar')
        stopPalavras.append('filho')
        stopPalavras.append('formular')
        stopPalavras.append('freitas')
        stopPalavras.append('fundamental')
        stopPalavras.append('gilmara')
        stopPalavras.append('gravidez')
        stopPalavras.append('gravido')
        stopPalavras.append('gusmao')
        stopPalavras.append('hipotese')
        stopPalavras.append('histori')
        stopPalavras.append('historia')
        stopPalavras.append('historiar')
        stopPalavras.append('historico')
        stopPalavras.append('hoje')
        stopPalavras.append('horar')
        stopPalavras.append('hospital')
        stopPalavras.append('hospitalar')
        stopPalavras.append('hospitalizacao')
        stopPalavras.append('idade')
        stopPalavras.append('id')
        stopPalavras.append('ig18')
        stopPalavras.append('ig37')
        stopPalavras.append('ig9')
        stopPalavras.append('ignorar')
        stopPalavras.append('igual')
        stopPalavras.append('impressao')
        stopPalavras.append('indice')
        stopPalavras.append('infectologista')
        stopPalavras.append('informacao')
        stopPalavras.append('informar')
        stopPalavras.append('ingerir')
        stopPalavras.append('instituicao')
        stopPalavras.append('instituto')
        stopPalavras.append('internacao')
        stopPalavras.append('internamento')
        stopPalavras.append('internar')
        stopPalavras.append('investigacao')
        stopPalavras.append('investigar')
        stopPalavras.append('irar')
        stopPalavras.append('irm')
        stopPalavras.append('irma')
        stopPalavras.append('irmao')
        stopPalavras.append('itabaiana')
        stopPalavras.append('jaguare')
        stopPalavras.append('janeiro')
        stopPalavras.append('janine')
        stopPalavras.append('joao')
        stopPalavras.append('jose')
        stopPalavras.append('josy')
        stopPalavras.append('julho')
        stopPalavras.append('juliete')
        stopPalavras.append('junho')
        stopPalavras.append('juntamente')
        stopPalavras.append('kg')
        stopPalavras.append('laboartoriais')
        stopPalavras.append('laboratorial')
        stopPalavras.append('laboratorias')
        stopPalavras.append('laboratorio')
        stopPalavras.append('lacen')
        stopPalavras.append('lactente')
        stopPalavras.append('laudo')
        stopPalavras.append('lauro')
        stopPalavras.append('lembrar')
        stopPalavras.append('levantar')
        stopPalavras.append('levar')
        stopPalavras.append('like')
        stopPalavras.append('m30')
        stopPalavras.append('macho')
        stopPalavras.append('mail')
        stopPalavras.append('maio')
        stopPalavras.append('major')
        stopPalavras.append('mamao')
        stopPalavras.append('maranhao')
        stopPalavras.append('marco')
        stopPalavras.append('masculino')
        stopPalavras.append('materni')
        stopPalavras.append('maternidade')
        stopPalavras.append('materno')
        stopPalavras.append('meireles')
        stopPalavras.append('medir')
        stopPalavras.append('mensurar')
        stopPalavras.append('mencao')
        stopPalavras.append('merecer')
        stopPalavras.append('mg')
        stopPalavras.append('mim')
        stopPalavras.append('ml')
        stopPalavras.append('mm3')
        stopPalavras.append('mmhg')
        stopPalavras.append('morador')
        stopPalavras.append('mostrar')
        stopPalavras.append('municipal')
        stopPalavras.append('municipio')
        stopPalavras.append('municpal')
        stopPalavras.append('mutirao')
        stopPalavras.append('nome')
        stopPalavras.append('notar')
        stopPalavras.append('notfic')
        stopPalavras.append('notificacao')
        stopPalavras.append('notificar')
        stopPalavras.append('noto')
        stopPalavras.append('novembro')
        stopPalavras.append('nph')
        stopPalavras.append('o80')
        stopPalavras.append('observacao')
        stopPalavras.append('observar')
        stopPalavras.append('obter')
        stopPalavras.append('obtido')
        stopPalavras.append('ocorrer')
        stopPalavras.append('odor')
        stopPalavras.append('ofertar')
        stopPalavras.append('ola')
        stopPalavras.append('osvaldo')
        stopPalavras.append('outubro')
        stopPalavras.append('p')
        stopPalavras.append('p0')
        stopPalavras.append('p50')
        stopPalavras.append('p5915')
        stopPalavras.append('p706')
        stopPalavras.append('pa')
        stopPalavras.append('pai')
        stopPalavras.append('paiente')
        stopPalavras.append('pantanal')
        stopPalavras.append('paraiba')
        stopPalavras.append('parceiro')
        stopPalavras.append('parecer')
        stopPalavras.append('patente')
        stopPalavras.append('paulo')
        stopPalavras.append('pc')
        stopPalavras.append('pedir')
        stopPalavras.append('pedriatras')
        stopPalavras.append('perceber')
        stopPalavras.append('perceptivel')
        stopPalavras.append('pereira')
        stopPalavras.append('periodo')
        stopPalavras.append('permitir')
        stopPalavras.append('pescador')
        stopPalavras.append('pesquisar')
        stopPalavras.append('pessoa')
        stopPalavras.append('pessoal')
        stopPalavras.append('planilha')
        stopPalavras.append('podendo')
        stopPalavras.append('policia')
        stopPalavras.append('possibilidade')
        stopPalavras.append('preescrito')
        stopPalavras.append('preferir')
        stopPalavras.append('presidiario')
        stopPalavras.append('primar')
        stopPalavras.append('profissional')
        stopPalavras.append('prontuario')
        stopPalavras.append('prontuarios')
        stopPalavras.append('protocolo')
        stopPalavras.append('protuario')
        stopPalavras.append('quaestionario')
        stopPalavras.append('quantidade')
        stopPalavras.append('questionario')
        stopPalavras.append('realata')
        stopPalavras.append('receber')
        stopPalavras.append('recife')
        stopPalavras.append('recordar')
        stopPalavras.append('registrar')
        stopPalavras.append('registro')
        stopPalavras.append('relatar')
        stopPalavras.append('relato')
        stopPalavras.append('relatorio')
        stopPalavras.append('revelar')
        stopPalavras.append('revisao')
        stopPalavras.append('roberto')
        stopPalavras.append('sair')
        stopPalavras.append('sala')
        stopPalavras.append('salvador')
        stopPalavras.append('samara')
        stopPalavras.append('santo')
        stopPalavras.append('secretariar')
        stopPalavras.append('secundario')
        stopPalavras.append('seguinte')
        stopPalavras.append('seguir')
        stopPalavras.append('semanal')
        stopPalavras.append('semanss')
        stopPalavras.append('semestre')
        stopPalavras.append('servico')
        stopPalavras.append('setembro')
        stopPalavras.append('silvar')
        stopPalavras.append('silviano')
        stopPalavras.append('soicitado')
        stopPalavras.append('solange')
        stopPalavras.append('soliciotado')
        stopPalavras.append('solicitar')
        stopPalavras.append('solicitodo')
        stopPalavras.append('solteiro')
        stopPalavras.append('souza')
        stopPalavras.append('sr')
        stopPalavras.append('style"font')
        stopPalavras.append('sul')
        stopPalavras.append('sumario')
        stopPalavras.append('resultar')
        stopPalavras.append('tecnica')
        stopPalavras.append('tecnicamente')
        stopPalavras.append('tecnico')
        stopPalavras.append('tel')
        stopPalavras.append('telefonar')
        stopPalavras.append('telefonico')
        stopPalavras.append('telefonicos')
        stopPalavras.append('testar')
        stopPalavras.append('tio')
        stopPalavras.append('tornar')
        stopPalavras.append('trabalhar')
        stopPalavras.append('transcorrer')
        stopPalavras.append('transcrever')
        stopPalavras.append('transferir')
        stopPalavras.append('tratamento')
        stopPalavras.append('tratar')
        stopPalavras.append('trimestre')
        stopPalavras.append('unidade')
        stopPalavras.append('universitario')
        stopPalavras.append('usuaria')
        stopPalavras.append('usuario')
        stopPalavras.append('utilizar')
        stopPalavras.append('valenca')
        stopPalavras.append('vestir')
        stopPalavras.append('viagem')
        stopPalavras.append('vigilancia')
        stopPalavras.append('vir')
        stopPalavras.append('visitar')
        
        stopPalavras.append("a")
        stopPalavras.append("e")
        stopPalavras.append("o")
        stopPalavras.append("m")
        stopPalavras.append("d")
        stopPalavras.append("v")
        stopPalavras.append("l")
        stopPalavras.append("algum")
        stopPalavras.append("apresentando")
        stopPalavras.append("apresentar")
        stopPalavras.append("aspecto")
        stopPalavras.append("aspectos")
        stopPalavras.append("associado")
        stopPalavras.append("associar")
        stopPalavras.append("atual")
        stopPalavras.append("avaliacao")
        stopPalavras.append("biometria")
        stopPalavras.append("aparente")
        stopPalavras.append("caracteristico")
        stopPalavras.append("caracteriza-se")
        stopPalavras.append("caracterizacao")
        stopPalavras.append("cm")
        stopPalavras.append("compativeis")
        stopPalavras.append("compativel")
        stopPalavras.append("comunicar")
        stopPalavras.append("considerar")
        stopPalavras.append("corresponder")
        stopPalavras.append("datada")
        stopPalavras.append("dezembro")
        stopPalavras.append("dia")
        stopPalavras.append("especificacao")
        stopPalavras.append("havia")
        stopPalavras.append("moderar")
        stopPalavras.append("provavelmente")
        stopPalavras.append("relacionar")
        stopPalavras.append("relacionado")
        stopPalavras.append("representar")
        stopPalavras.append("sugestivo")
        stopPalavras.append("umar")
        stopPalavras.append("visibilizacao")
        stopPalavras.append("visto")
        stopPalavras.append("visualizar")
        stopPalavras.append("ultima")
        stopPalavras.append("unica")
        stopPalavras.append("unico")
        stopPalavras.append("voluntario")
        stopPalavras.append("evidenciar")
        stopPalavras.append("exame")
        stopPalavras.append("imagem")
        stopPalavras.append("indicar")
        stopPalavras.append("obs")
        stopPalavras.append("sugerimos")
        stopPalavras.append("sugerir")
        stopPalavras.append("semana")
        stopPalavras.append("situacao")
        stopPalavras.append("sobretudo")
        stopPalavras.append("substanciar")
        stopPalavras.append("sugerindo")
        stopPalavras.append("assumir")
        stopPalavras.append("completar")
        stopPalavras.append("derecionado")
        stopPalavras.append("durante")
        stopPalavras.append("encontrar")
        stopPalavras.append("esclarecer")
        stopPalavras.append("esperado")
        stopPalavras.append("estudar")
        stopPalavras.append("evidente")
        stopPalavras.append("notadamente")
        stopPalavras.append("observam-se")
        stopPalavras.append('identificar')
        stopPalavras.append('outro')
        stopPalavras.append('paciente')
        stopPalavras.append('provavel')
        self.stopPalavras = stopPalavras
        self.mapa = {
        'area':'areas','atild':'atilde','apoptose':'reducao','antihvc':'hcv','antihtlv':'htlv','antihiv':'hiv','antihcv':'hcv','aghbs':'hbs','antihbs':'hbs','anti':'anticorpo','anteriormente':'anterior','anteceder':'anterior','antecedente':'anterior','ant':'anterior','anencefalia':'anencefalo','anamalia':'anormal','anormalidade':'anormal','anomalidade':'anormal','anomalia':'anormal','amnioti':'amniotico','amni':'amniotico','aminiotico':'amniotico','ambulatorio':'ambulatorial','altracoe':'anormal','altercoes':'anormal','aintihcv':'hcv','abdomen':'abdome','abdominal':'abdome','abortar':'aborto','abaixar':'abaixo','acentuacao':'acentuada','acentuar':'acentuada','acentuda':'acentuada','agenesia':'agnesia','acidar':'acido','administracao':'administrar','adoecimento':'doenca','afilamento':'discreto','agravar':'severo','alteracao':'anormal','alcool':'alcoolismo','alcoolica':'alcoolismo','alcoolicas':'alcoolismo','alcoolico':'alcoolismo','alcoollica':'alcoolismo','aumentar':'crescimento','aumento':'crescimento','agrupar':'agrupadas','alargamento':'crescimento','alta':'acentuada','alto':'acentuada','altas':'acentuada','amniotica':'amniotico','anecoica':'anecoico','anormais':'anormal','arterial':'arteria','arterias':'arteria','assimetrica':'assimetria','assimetrico':'assimetria', 'assimetricos':'assimetria','atrofia':'reducao','atrofiar':'reducao','alteracoe':'anormal','alteracoes':'anormal','atrial':'atrio','atrofico':'reducao', 'artra':'artropatia','artralgia':'artropatia','artrogripose':'artropatia','articular':'articulacao','ausente':'ausencia','adelgacamento':'reducao','afrofia':'reducao',
        'bpm':'bcf','bilitest':'bilirrubina','bebido':'beber','bebiba':'beber','barriga':'abdome','baixar':'reducao','baar':'ebv','bilatera':'bilateral','bilaterais':'bilateral','bilateralmente':'bilateral','branca':'branco',
        'cmvigg':'citomegalovirus','cvm':'citomegalovirus','cutis':'cutaneo','cuteneo':'cutaneo','curto':'discreto','cronicas':'cronica','cranio':'cefalico','crak':'crack','contatos':'contato','constatar':'confirmacao','consangu':'consanguinidade','congenito':'congenita','congenitas':'congenita','cong':'congenita','confirmatorio':'confirmacao','comprobatorio':'confirmacao','colecao':'variadas','cmvi':'citomegalovirus','cmvconsta':'citomegalovirus','cmv':'citomegalovirus','citomrgalovirus':'citomegalovirus','citomegalovir':'citomegalovirus','citomegalovi':'citomegalovirus','citomegalosvirus':'citomegalovirus','citomagalovirus':'citomegalovirus','citomeg':'citomegalovirus','circunfer':'circunferencia','circ':'circunferencia','chuikungunya':'chikungunya','chk':'chikungunya','chikungunia':'chikungunya','chikungunha':'chikungunya','chikun':'chikungunya','chiku':'chikungunya','chik':'chikungunya','chicungunya':'chikungunya','cesareo':'cesarea','cerebr':'cerebro','centralizar':'centralizacao','cefalicas':'cefalico','cefalicac':'cefalico','cefalica':'cefalico','cefalecina':'cefalexina','carniana':'cefalico','cardiopatia':'cardiaco','cardiop':'cardiaco','cardiaca':'cardiaco','calficicacoes':'calcificacao','calcificacoesreducao':'calcificacao','calcificacoe':'calcificacao','calcificaco':'calcificacao','calcifi':'calcificacao','calc':'calcificacao','cafalica':'cefalico','cabeca':'cefalico','cabecas':'cefalico','calcificacoes':'calcificacao','calcificar':'calcificacao','calsificacao':'calcificacao','capsular':'capsula','capsulo':'capsula','centrar':'centralizacao','cerebelar':'cerebelo','cerebelarcranio':'cerebelo','cerebrais':'cerebro','cerebral':'cerebro','cerebra':'cerebro', 'circunvolucao':'circunferencia', 'cistica':'cisto','cisticas':'cisto','cistico':'cisto','cistos':'cisto', 'compensataria':'compensatoria','conclusao':'confirmacao','confirmada':'confirmacao','confirmar':'confirmacao','cornar':'corneo','corno':'corneo','cornos':'corneo','corticais':'cortex','cortical':'cortex','corticos':'cortex','corporal':'corpo','craniana':'cranio','craniano':'cranio',
        'duplicidade':'duplo','doer':'dor','doen':'doenca','disturbios':'anormal','disponiveis':'disponivel','dilat':'crescimento','dignostico':'confirmacao','dignosticada':'confirmacao','diferente':'anormal','diarreico':'diarreia','diagnosticas':'diagnostico','diagnosticar':'diagnostico','diagnostica':'diagnostico','diagnostic':'diagnostico','diag':'diagnostico','detectavel':'deteccao','detectar':'deteccao','detec':'deteccao','destruicao':'anormal','desaparecer':'reducao','dengu':'dengue','deng':'dengue','degeneracao':'reducao','deformidade':'anormal','deformar':'anormal','deficit':'reducao','deficiencia':'reducao','dandy':'dandy-walker','dondy':'dandy-walker','walker':'dandy-walker','definidas':'confirmacao','definido':'confirmacao','destaca':'acentuada','determinando':'confirmacao','diametro':'circunferencia','diametros':'circunferencia','difusamente':'difusa','difusas':'difusa','difuso':'difusa','dilatar':'crescimento','dilatacao':'crescimento','dimensoes':'dimensao','diminuido':'reducao','diminuicao':'reducao','discreta':'discreto','discretamente':'discreto','dimorfismo':'dismorfismo','distribuidas':'distribuida','distribuir':'distribuida','delgado':'discreto','desproporcao':'anormal','dilatacao':'crescimento','diminuicao':'reducao','disproporcao':'anormal',
        'excessivo':'severo','exatema':'exantema','exantematima':'exantema','exantematico':'exantema','exantematicas':'exantema','exantematica':'exantema','evidencia':'confirmacao','etiologia':'etiologico','estreito':'discreto','estabelecido':'confirmacao','espont':'espontaneo','espalhar':'esparso','espaco':'esparso','epstein':'ebv','encefalico':'encefalo','ecograficos':'ecografico','ecografia':'ecografico','ecocardioigrama':'ecocardiograma','ecocardiog':'ecocardiograma','ecocardiagrama':'ecocardiograma','ecogenicidade':'ecogenico','elevar':'acentuada','encefalica':'encefalico','encefalo':'encefalico','esq':'esquerdo','esquer':'esquerdo','encefal':'encefalo','encefalico':'encefalo','enchimento':'crescimento','esparsas':'discreto','esquerda':'esquerdo','esquerdar':'esquerdo','estreitamento':'reducao',
        'fumar':'tabaco','fumante':'tabaco','fraco':'discreto','feto2':'fetal','feto1':'fetal','febril':'febre','febrel':'febre','familiar':'familia','falha':'anormal','fechamento':'fechar','fusao':'fechar','face':'facial','feto':'fetal','fissurar':'fissuras','focos':'foco','frontais':'frontal',
        'glicose':'glicemia','glic':'glicemia','gicemia':'glicemia','gestcao':'gestacao','gestacional':'gestacao','gestaca':'gestacao','gestac':'gestacao','gesta':'gestacao','gest':'gestacao','giros':'giro','giral':'giro','grosseiras':'grosseiro',
        'hsag':'hbs','hivs':'hiv','anti-hiv':'hiv','hipoxico':'hipoxia','hipotireioidismo':'hipotireoidismo','hipoplasicas':'hipoplasico','hipertesnao':'hipertensao','hipertenso':'hipertensao','hipertensivo':'hipertensao','hiperextensao':'crescimento','hiperestensao':'crescimento','heterogenea':'heterogeneo','herpes':'hsv','hepb':'hbs','hepatitec':'hcv','hepatiteb':'hbs','hepaptite':'hepatite','hemmorragia':'hemorragia','hemoglobia':'hemoglobina','hematrocrito':'hematocrito','hbc':'hcv','hbshg':'hbs','hbsg':'hbs','hbsag':'hbs','hbcv':'hcv','habitual':'comumente','hemisferios':'hemisferio','hemorragico':'hemorragia','hidroanencefalia':'hidrocefalia','hidranencefalia':'hidrocefalia','hiperecoicos':'hiperecoicas','hipodensa':'hipodensidade','hipoplasia':'reducao','holoprosecefalia':'holoprosencefalia',
        'irritabilida':'irritabilidade','irradiar':'esparso','intrautero':'intrauterino','intrauterinas':'intrauterino','intrauterina':'intrauterino','intracranianas':'intracraniana','intracerebral':'intracraniana','intercorrencias':'intercorrencia','intercorr':'intercorrencia','intenso':'severo','insuficiente':'reducao','insuficiencia':'reducao','infec':'infeccao','inespecificas':'inespecifico','indeterminar':'inderteminado','incomple':'incompleto','incomp':'incompleto','inchaco':'crescimento','implatacao':'implantacao','ilicitas':'ilicito','igm0':'igm','igg10':'igg','identificacao':'confirmacao','icterico':'ictericia','involucao':'reducao','inespecfico':'inespecifico','inespecificos':'inespecifico','inexpecifica':'inespecifico','infecciosa':'infeccao','infeccioso':'infeccao','injuria':'anormal','irregular':'anormal','interior':'interno','isquemica':'isquemico',
        'luxacao':'crescimento','linf':'linfocitos','leuco':'leucocito','leucocitos18':'leucocito','leucocitos':'leucocito','lesao':'anormal','lacerar':'anormal','laterais':'lateral','lisenfalia':'lisencefalia','later':'lateral','lados':'lateral','lineares':'linear','lisencefalias':'lisencefalia','lisencefalicas':'lisencefalia','linha':'linear','lobo':'lobos','lobolos':'lobos','localizar':'localizadas',
        'morfologico':'morfologia','mon':'monocitos','minimo':'reducao','microoftalmia':'microftalmia','microcelafia':'microcefalia','microcefali':'microcefalia','micr':'microcefalia','micro':'microcefalia','micricefalia':'microcefalia','microcalcificacao':'calcificacao','mental':'cognitivo','medicar':'medicamentar','medicamento':'medicamentar','medicacoes':'medicamentar','medicacao':'medicamentar','mediar':'medicacao','mediante':'medicacao','malformaca':'malformacao','malforma':'malformacao','malfor':'malformacao','malfomalcao':'malformacao','magnetico':'rm','magnetica':'rm','macrocalcificacoes':'calcificacao','microcalcificacoes':'calcificacao','microcefalico':'microcefalia','microcrania':'microcefalia','morfas':'morfologico','morfologica':'morfologico','multiplas':'variadas','multiplos':'variadas','multiplo':'variadas',
        'nr':'negativo','normalidade':'negativo','normalida':'negativo','normal':'negativo','norm':'negativo','nervosoatipico':'nervoso','nenhum':'negativo','negativar':'negativo','negati':'negativo','neg':'negativo','necessarios':'necessitar','necessario':'necessitar','nascido':'nascimento','nascer':'nascimento','nasc':'nascimento','nasal':'nariz','nuclear':'nucleo','nucleos':'nucleo',
        'ovalar':'oval','oligodramnia':'oligodramnio','oligamnio':'oligodramnio','ok':'negativo','oftamologica':'oftalmologia','oftalmologico':'oftalmologia','ocupitais':'occipital','occiptal':'occipital','obstetrico':'obstetrica','obstretica':'obstetrica','obstetri':'obstetrica','obstetra':'obstetrica','occipitais':'occipital','oligoamnio':'oligodramnio','oligodremnia':'oligodramnio',
        'plaq':'plaqueta','purido':'prurir','puerpera':'puerperio','puericultur':'puericultura','pruriginoso':'prurir','proteinas':'proteina','proseguir':'prosseguir','proliferar':'crescimento','presentar':'presenca','preenchimento':'preencher','possuir':'positivo','positivar':'positivo','pos':'positivo','polihidraminia':'polidramnio','persistencia':'persistente','perim':'perimetro','percetil':'percentil','patologico':'anormal','patologia':'anormal','parvo':'parvovirus','parequimatosas':'parenquima','parequima':'parenquima','parenqu':'parenquima','paremica':'parenquima','parametros':'padrao','parametro':'padrao','padr':'padrao','paquigirico':'paquigiria','parcialmente':'discreto','parcial':'discreto','paremquima':'parenquima','parenquimatosas':'parenquima','parenquimatoso':'parenquima','pariental':'parietal','pequenas':'discreto','periventricularaes':'periventricular','periventriculares':'periventricular','podend':'podendo','porcoes':'porcao','predominando':'acentuada','predominio':'acentuada','predominantemente':'acentuada','proeminencia':'acentuada','proeminente':'acentuada','perda':'ausencia','parietais':'parietal','pequena':'discreto','pequeno':'discreto','posteriores':'posterior',
        'quadruplo':'quadruplicar',
        'rinite':'alergico','rgico':'alergico','respiratorio':'respiracao','repetitivo':'repeticao','rubeolar':'rubeolar','rubeolaigm':'rubeola','rub':'rubeola','rubeol':'rubeola','rnm':'rm','rmm':'rm','restri':'restricao','ressonancia':'rm','resist':'resistencia','regante':'positivo','reg':'positivo','redu':'reducao','reativo':'positivo','realizdos':'realizar','realizacao':'realizar','realiz':'realizar','realiozados':'realizar','realiazados':'realizar','reagnete':'positivo','reagentetoxoplasmose':'toxo','reagenstes':'positivo','reagen':'positivo','reag':'positivo','rapidos':'rapido','radiar':'crescimento','reabsorcao':'reducao','regioes':'regiao','reduzir':'reducao','realizada':'realizar','realizou':'realizar','remanescente':'discreto',
        'suspeitar':'suspeito','significativo':'severo','suseptivel':'suscetivel','sucorticais':'subcortical','subcorticais':'subcortical','stoch':'storch','sorologicos':'sorologia','sorologico':'sorologia','sorologai':'sorologia','sorol':'sorologia','sonografico':'ultrasonografia','sonografias':'ultrasonografia','sisilis':'sifilis','sintomatologia':'sintoma','sindromica':'sindrome','sindrmoe':'sindrome','sinalizacao':'sinal','sifili':'sifilis','sifiles':'sifilis','sifiis':'sifilis','scaner':'scanner','sanguineo':'sangue','sinais':'sinal','segmento':'segmentar','seguimento':'segmentar','significativa':'severo','sequelar':'anormal','sequela':'anormal','simetrica':'simetrico','sulcos':'sulco','supratentarial':'supratentorial','supratentoreal':'supratentorial','supratentoriais':'supratentorial',
        'trasnsfontanela':'transfontanela','transfontonela':'transfontanela','transfontene':'transfontanela','transfontanelar':'transfontanela','transfontalena':'transfontanela','transfonta':'transfontanela','transfont':'transfontanela','transfon':'transfontanela','toxoplsmose':'toxo','toxoplasmpose':'toxo','toxoplasmose':'toxo','toxoplasmo':'toxo','toxoplasma':'toxo','toxoplasm':'toxo','toxoplamose':'toxo','toxopla':'toxo','toxiinfeccao':'toxo','tox':'toxo','torch':'storch','toracico':'torax','tc':'tomografia','tomograficos':'tomografia','tomografico':'tomografia','tabagista':'tabaco','tabagismo':'tabaco','talamica':'talamo','talar':'talamo','tenue':'discreto','tenues':'discreto','temporais':'temporal','tentoriais':'temporal','torchs':'torch','torto':'anormal',
        'ustf':'transfontanela','ust':'transfontanela','usgtransfontonela':'transfontanela','usgtf':'transfontanela','usgt':'transfontanela','usgft':'transfontanela','usg':'ultrasonografia','usft':'transfontanela','usf':'ultrasonografia','ultrassons':'ultrasonografia','ultrassonograficos':'ultrasonografia','ultrassonografias':'ultrasonografia','ultrassonografia':'ultrasonografia','ultrassonog':'ultrasonografia','ultrassongrafia':'ultrasonografia','ultrasson':'ultrasonografia','ultrassom':'ultrasonografia','ultrasso':'ultrasonografia','ultrasonografias':'ultrasonografia','ultrasom':'ultrasonografia','ultras':'ultrasonografia',
        'virose':'virus','viral':'virus','ventroculomegalia':'ventriculomegalia','ventriculomagalia':'ventriculomegalia','vasoculopatia':'vasculopatia','variar':'variadas','varginal':'vagina','vaginal':'vagina','vacinal':'vacinar','variante':'variadas','ventricomegalia':'ventriculomegalia','ventricular':'ventriculo','ventriculos':'ventriculo','venix':'vermix','vermis':'vermix','vernix':'vermix','vasculopatias':'vasoculopatia','ventriculomagele':'ventroculomegalia','ventriculomegalia':'ventroculomegalia','ventricumegalia':'ventroculomegalia','ventriculomegalia':'ventroculomegalia','ventroculomegalia':'ventriculomegalia','volumar':'volume','volumetrica':'volume','volumetrico':'volume',
        'walter':'dandy-walker',
        'zikavirus':'zika','zica':'zika','zi':'zika'
        }
        self.mapaNeg = {'+':' positivo ','naõ':'não',"negativosnega":'negativos nega',' -\n':' negativo\n',"  ":" "," nao ":" não ", " n ":" não ", " ñ ":" não ",'ausencia':'ausência','ausensia':'ausência','ausênsia':'ausência','indetectavel':'indetectável','resultadonegativo':'resultado negativo','igmnegativo':'igm negativo','igm-':'igm negativo','iggreagente':'igg reagente','microcefalia-':'microcefalia negativa'}
        self.neg = ['-','ausente','perder','perda','descartado','descartar',"ausentar","ausencia","falta","faltar","sem","nao","nem",'negativo','negar','negativar',"nenhum",'indetectavel']

        self.nlp = spacy.load("pt_core_news_lg")
    
    def _getDocs(self,texts):
        def get_pattern(doc):
             #patern
            def verb(token):
                doc[token.i]._.is_neg=True
                for t in doc[token.i].children:
                    if t.dep_=='obj':
                        #print(t.text+" pos: "+ t.dep_)
                        if ((t.pos_=='NOUN')or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                        if (t.pos_=='SCONJ') and (t._.is_neg==False):
                            sconj(t)
                    if t.dep_=='obl':
                        if ((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=='nsubj:pass':
                        if ((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=='advmod':
                        if (t.pos_=="ADV")and (t._.is_neg==False):
                            adv(t)
                    if t.dep_=='xcomp':
                        if ((t.pos_=="VERB")or(t.pos_=="AUX"))and (t._.is_neg==False):
                            verb(t)
            def noun(token):
                doc[token.i]._.is_neg=True
                if token.dep_=="xcomp":
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and(head._.is_neg==False):
                        noun(head)
                if token.dep_=='amod':
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and (head._.is_neg==False):
                        noun(head)
                    if (head.pos_=="ADJ")and(head._.is_neg==False):
                        adj(head)
                if token.dep_=='conj':
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and(head._.is_neg==False):
                        noun(head)
                if token.dep_=='nsubj':
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and(head._.is_neg==False):
                        noun(head)
                if token.dep_=='nmod':
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and(head._.is_neg==False):
                        noun(head)
                if token.dep_=='det':
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and(head._.is_neg==False):
                        noun(head)
                if token.dep_=="parataxis":
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and(head._.is_neg==False):
                        noun(head)
                if token.dep_=="appos":
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or(head.pos_=="PROPN"))and(head._.is_neg==False):
                        noun(head)
                for t in token.children:
                    if t.dep_=='conj':
                        if ((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=='amod':
                        if (t.pos_=="ADJ")and (t._.is_neg==False):
                            adj(t)
                        if ((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=="nsubj":
                        if((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=="nmod":
                        if((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=="det":
                        if((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=="parataxis":
                        if((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    if t.dep_=="parataxis":
                        if((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
                    
            def adj(token):
                doc[token.i]._.is_neg=True
                if token.dep_=="amod":
                    head = doc[token.i:token.i+1].root.head
                    if ((head.pos_=="NOUN")or (head.pos_=="PROPN"))and (head._.is_neg==False):
                        noun(head)
                    if (head.pos_=="ADJ")and (head._.is_neg==False):
                        adj(head)
                for t in token.children:
                    if t.dep_=="csubj":
                        if ((t.pos_=="VERB")or(t.pos_=="AUX"))and (t._.is_neg==False):
                            verb(t)
                    if t.dep_=='nsubj':
                        if(t.pos_=="ADJ")and (t._.is_neg==False):
                            adj(t)
                        if ((t.pos_=="NOUN")or (t.pos_=="PROPN"))and (t._.is_neg==False):
                            noun(t)
                
            def adv(token):
                doc[token.i]._.is_neg=True
                head = doc[token.i:token.i+1].root.head
                if ((head.pos_=="NOUN")or (head.pos_=="PROPN"))and (head._.is_neg==False):
                    noun(head)
                if ((head.pos_=="VERB")or(head.pos_=="AUX"))and (head._.is_neg==False):
                    verb(head)
                if (head.pos_=="ADJ")and (head._.is_neg==False):
                    adj(head)
                for t in token.children:
                    if t.dep_=="obl":
                        if((t.pos_=="NOUN")or(t.pos_=='PROPN'))and (t._.is_neg==False):
                            noun(t)
            def adp(token):
                doc[token.i]._.is_neg=True
                head = doc[token.i:token.i+1].root.head
                if ((head.pos_=="NOUN")or (head.pos_=="PROPN"))and (head._.is_neg==False):
                    noun(head)
            def sconj(token):
                doc[token.i]._.is_neg=True
        
            #start
            for token in doc:
                if (token.lemma_.lower() in self.neg) or (token._.new in self.neg):
                    if (token.pos_=="VERB") or (token.pos_=="AUX"):
                        verb(token)
                    if token.pos_=="ADV":
                        adv(token)
                    if token.pos_=="ADJ":
                        adj(token)
                    if token.pos_=="NOUN":
                        noun(token)
                    if token.pos_=="ADP":
                        adp(token)            
            return doc 
    
        def select_similar(doc):
            for token in doc:
                nome = token.lemma_.lower()
                nome = unidecode.unidecode(nome)
                if nome in self.mapa:
                    nome = self.mapa[nome]
                doc[token.i]._.new=nome
                if (token.pos_ == "VERB" or token.pos_ == "PROPN" or token.pos_ == 'ADJ' or token.pos_ == 'NOUN') and (token.is_alpha==True)  and (token.is_punct==False):
                #if (token.pos_ == "VERB" or token.pos_ == "PROPN" or token.pos_ == 'ADJ' or token.pos_ == 'NOUN')  and (token.is_punct==False):
                    
                    if (nome in self.stopPalavras)==False:
                        if (token._.new in self.neg)==False:
                            doc[token.i]._.is_select=True
            return doc
        
        TAG_RE = re.compile(r'<[^>]+>')
        TAG_RE2 = re.compile(r'&nbs[p]?;')
        TAG_RE3 = re.compile(r'&atilde;')
        pad1 = r'[a-zA-Z]+[=\-;\(\)./,:]'
        pad2 = r'[=\-;\(\)./,:][a-zA-Z]+'
        def remove_tags(text):
            text = TAG_RE.sub('', text)
            text = TAG_RE2.sub(' ', text)
            text = TAG_RE3.sub('ã', text)
            res = re.findall(pad1,text)
            for s in res:
                text = text.replace(s,s[0:-1]+' '+s[-1])
            res = re.findall(pad2,text)
            for s in res:
                text = text.replace(s,s[0]+' '+s[1:len(s)])
            return TAG_RE.sub('', text)
        
        for i in range(len(texts)):
            texts[i] = html.unescape(remove_tags(texts[i].strip().lower()))
            for key in self.mapaNeg.keys():
                texts[i] = texts[i].replace(key,self.mapaNeg[key])
        
        if 'ner' in self.nlp.pipe_names:
            self.nlp.disable_pipes("ner")

        Token.set_extension("is_neg", default=False,force=True)
        Token.set_extension("is_select", default=False,force=True)
        Token.set_extension("new", default=False,force=True)
        if 'select_similar' not in self.nlp.pipe_names:
            self.nlp.add_pipe(select_similar)
            self.nlp.add_pipe(get_pattern)
        
        return list(self.nlp.pipe(texts))
    
    def setWordsText(self,texts,limiar):
        self.docs = self._getDocs(list(texts))
        lista_total=[]
        for d in self.docs:
            l = []
            for t in d:
                if t._.is_select:
                    l.append(t._.new)
                    
            lista_total.append(l)
        words_total={}
        for l in lista_total:
            tag=True
            for p in l:
                if p not in words_total:
                    words_total[p]=1
                else:
                    if tag:
                        tag=False
                        words_total[p]=words_total[p]+1
        lista=list(words_total.keys())
        for k in lista:
            if words_total[k]<limiar:
                words_total.pop(k)
        lista=list(words_total.keys())
        self.listaWords = lista
        return lista
    
    def setWords(self,lista):
        self.listaWords = lista
        
    
    def getDataframe(self,dataFrame,texts):
        banco = dataFrame.copy()
        tam = len(dataFrame)
        self.docs = self._getDocs(texts)
        lista_total=[]
        neg_total =[]
        for d in self.docs:
            l = []
            n = []
            for t in d:
                if t._.is_select:
                    l.append(t._.new)
                    if t._.is_neg:
                        n.append(False)
                    else:
                        n.append(True)
            lista_total.append(l)
            neg_total.append(n)
        
        for word in self.listaWords:
            lvar = np.zeros(tam,dtype='int64')
            for i in range(tam):
                tag=True
                for l in range(len(neg_total[i])):
                    if lista_total[i][l]==word:
                        if neg_total[i][l]:
                            lvar[i]=2
                            tag=False
                        else:
                            if lvar[i]!=2:
                                lvar[i]=0
                                tag=False
                if tag:
                    lvar[i]=1
            aux=word+'_word'
            banco[aux] = lvar
        return banco
    
    def getWord(self):
        return self.listaWords
        