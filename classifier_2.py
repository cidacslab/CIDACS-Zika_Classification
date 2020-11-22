# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 08:15:03 2020

@author: rafae
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
import unidecode
import string
#import xgboost as xgb
from sklearn.metrics import accuracy_score,precision_score, recall_score
from sklearn.model_selection import train_test_split
import pickle as pk
from sklearn.preprocessing import MinMaxScaler
#import arff
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report ,accuracy_score


seed = 1234
XDf = pd.read_csv("banco_total2.csv",index_col=0)  
X = XDf[XDf.typeClass=="group2"].copy()
X = X.fillna(-9)   
X.sexo.replace(['Ignorado','Não Informado'],[-9,-9],inplace=True) 
X['sexo_miss'] = X['sexo'].copy()
X.sexo.replace(['Feminino','Masculino',-9],[0,1,0],inplace=True)
X.sexo_miss.replace(['Feminino','Masculino',-9],[0,0,1],inplace=True)     
X['tamanhoCabe_miss'] = X['tamanhoCabe'].copy()
X.loc[X.tamanhoCabe!=-9,'tamanhoCabe_miss'] = 0 
X.tamanhoCabe_miss.replace([-9],[1],inplace=True) 
X.tamanhoCabe.replace([-9],[32],inplace=True)  
X.classFeto.replace(['Não se aplica'],[-9],inplace=True)
X['classFeto_miss'] = X.classFeto.copy()
X.classFeto.replace(['Termo','Pré-Termo','Pós-Termo',-9],[1,0,2,0],inplace=True)   
X.loc[X.classFeto_miss!=-9,'classFeto_miss'] =0  
X.loc[X.classFeto_miss==-9,'classFeto_miss'] =1  
X["micro_miss"] = X.micro.copy()
X.micro.replace([-9],[0],inplace=True)
X.loc[X.micro_miss!=-9,'micro_miss']=0
X.loc[X.micro_miss==-9,'micro_miss']=1   
X.NV_TC_MICRO.replace(['SIM',-9],[1,0],inplace=True)
X.NV_Storch.replace(['4.Não fez nenhum exame para STRC'],[-9],inplace=True)
X['NV_Storch_miss']=X.NV_Storch.copy()
X.NV_Storch.replace(['2.Negativo para todos os STRC','3.Negativo para 1-3 STRC','1.Positivo para pelo menos 1 STRC',-9],[0,1,2,1],inplace=True)
X.loc[X.NV_Storch_miss!=-9,'NV_Storch_miss']=0
X.loc[X.NV_Storch_miss==-9,'NV_Storch_miss']=1
X['NV_sifilis_miss']=X.NV_sifilis.copy()
X.NV_sifilis.replace(['NR','Reagente',-9],[0,1,0],inplace=True)
X.loc[X.NV_sifilis_miss!=-9,'NV_sifilis_miss']=0
X.loc[X.NV_sifilis_miss==-9,'NV_sifilis_miss']=1
X['NV_TOXO_miss'] = X.NV_TOXO.copy()
X.NV_TOXO.replace(['NR','Reagente',-9],[0,1,0],inplace=True)
X.loc[X.NV_TOXO_miss!=-9,'NV_TOXO_miss']=0
X.loc[X.NV_TOXO_miss==-9,'NV_TOXO_miss']=1
X['NV_CMV_miss'] = X.NV_CMV.copy()
X.NV_CMV.replace(['NR','IgG reagente',-9],[0,1,1],inplace=True)
X.loc[X.NV_CMV_miss!=-9,'NV_CMV_miss']=0
X.loc[X.NV_CMV_miss==-9,'NV_CMV_miss']=1
X['NV_DENGUE_miss'] = X.NV_DENGUE.copy()
X.NV_DENGUE.replace(['NR','Reagente',-9],[0,1,0],inplace=True)
X.loc[X.NV_DENGUE_miss!=-9,'NV_DENGUE_miss']=0
X.loc[X.NV_DENGUE_miss==-9,'NV_DENGUE_miss']=1
X['NV_CHIK_miss'] = X.NV_CHIK.copy()
X.NV_CHIK.replace(['NR','Reagente',-9],[0,1,0],inplace=True)
X.loc[X.NV_CHIK_miss!=-9,'NV_CHIK_miss']=0
X.loc[X.NV_CHIK_miss==-9,'NV_CHIK_miss']=1
del X['count_storch']
X.NV_USG_MICRO.replace(['SIM',-9],[1,0],inplace=True)
X.NV_RM_MICRO.replace(['SIM',-9],[1,0],inplace=True)
X['NV_USG_RESULT_miss'] = X.NV_USG_RESULT.copy()
X.NV_USG_RESULT.replace(['Normal','Indeterminado','Alterado',-9],[0,1,2,0],inplace=True)
X.loc[X.NV_USG_RESULT_miss!=-9,'NV_USG_RESULT_miss']=0
X.loc[X.NV_USG_RESULT_miss==-9,'NV_USG_RESULT_miss']=1
X['NV_TC_RESULT_miss'] = X.NV_TC_RESULT.copy()
X.NV_TC_RESULT.replace(['Indeterminado','Alterado',-9],[0,1,1],inplace=True)
X.loc[X.NV_TC_RESULT_miss!=-9,'NV_TC_RESULT_miss']=0
X.loc[X.NV_TC_RESULT_miss==-9,'NV_TC_RESULT_miss']=1
X['NV_RM_RESULT_miss'] = X.NV_RM_RESULT.copy()
X.NV_RM_RESULT.replace(['Indeterminado','Alterado',-9],[0,1,1],inplace=True)
X.loc[X.NV_RM_RESULT_miss!=-9,'NV_RM_RESULT_miss']=0
X.loc[X.NV_RM_RESULT_miss==-9,'NV_RM_RESULT_miss']=1
X.missImagem.replace([-9],[0],inplace=True)
# Y
Y = X.casegr.copy()
del X['casegr']
del X['classFinal']
del X['typeClass']
Y.replace(['Discarded','Somewhat probable','Moderately probable','Highly probable'],[0,1,2,3],inplace=True)
Y.astype('int64')
# text
text = X.texto.copy()
# save data
file = open('Xclassific2.dat','wb')
pk.dump(X,file)
file.close()
file = open('Yclassific2.dat','wb')
pk.dump(Y,file)
file.close()
del X['texto']
# Convert int64

# NLP
def similar(tex,mapa):
    tex = unidecode.unidecode(tex)
    
    if tex in mapa:
        tex = mapa[tex]
    return tex 
def extrair(tex,mapa,ponto):
    token = nlp(tex)
    doc = token
    token = [word for word in token if word.like_num==False]
    token = [word.lemma_.lower().strip() if word.lemma_ != "-PRO-" else word.lower_ for word in token]
    token = [word for word in token if similar(word,mapa) not in stopPalavras and word not in ponto]
    token = [similar(word,mapa) for word in token]
    return token, doc
mapa = {
        'atild':'atilde','apoptose':'reducao','antihvc':'hcv','antihtlv':'htlv','antihiv':'hiv','antihcv':'hcv','aghbs':'hbs','antihbs':'hbs','anti':'anticorpo','anteriormente':'anterior','anteceder':'anterior','antecedente':'anterior','ant':'anterior','anencefalia':'anencefalo','anamalia':'anormal','anormalidade':'anormal','anomalidade':'anormal','anomalia':'anormal','amni':'amniotico','aminiotico':'amniotico','ambulatorio':'ambulatorial','altracoe':'anormal','altercoes':'anormal','aintihcv':'hcv','abdomen':'abdome','abdominal':'abdome','abortar':'aborto','abaixar':'abaixo','acentuacao':'acentuada','acentuar':'acentuada','acentuda':'acentuada','agenesia':'agnesia','acidar':'acido','administracao':'administrar','adoecimento':'doenca','afilamento':'discreto','agravar':'severo','alteracao':'anormal','alcool':'alcoolismo','alcoolica':'alcoolismo','alcoolicas':'alcoolismo','alcoolico':'alcoolismo','alcoollica':'alcoolismo','aumentar':'crescimento','aumento':'crescimento','agrupar':'agrupadas','alargamento':'crescimento','alta':'acentuada','alto':'acentuada','altas':'acentuada','amniotica':'amniotico','anecoica':'anecoico','anormais':'anormal','arterial':'arteria','arterias':'arteria','assimetrica':'assimetria','assimetrico':'assimetria', 'assimetricos':'assimetria','atrofia':'reducao','atrofiar':'reducao','alteracoes':'alteracao','atrial':'atrio','atrofico':'reducao', 'artra':'artropatia','artralgia':'artropatia','artrogripose':'artropatia','articular':'articulacao','ausente':'ausencia','adelgacamento':'reducao','afrofia':'reducao',
        'bpm':'bcf','bilitest':'bilirrubina','bebido':'beber','bebiba':'beber','barriga':'abdome','baixar':'reducao','baar':'ebv','bilatera':'bilateral','bilaterais':'bilateral','bilateralmente':'bilateral','branca':'branco',
        'cvm':'citomegalovirus','cutis':'cutaneo','cuteneo':'cutaneo','curto':'discreto','cronicas':'cronica','cranio':'cefalico','crak':'crack','contatos':'contato','constatar':'confirmacao','consangu':'consanguinidade','congenito':'congenita','congenitas':'congenita','cong':'congenita','confirmatorio':'confirmacao','comprobatorio':'confirmacao','colecao':'variadas','cmvi':'citomegalovirus','cmvconsta':'citomegalovirus','cmv':'citomegalovirus','citomrgalovirus':'citomegalovirus','citomegalovir':'citomegalovirus','citomegalovi':'citomegalovirus','citomegalosvirus':'citomegalovirus','citomagalovirus':'citomegalovirus','citomeg':'citomegalovirus','circunfer':'circunferencia','circ':'circunferencia','chuikungunya':'chikungunya','chk':'chikungunya','chikungunia':'chikungunya','chikungunha':'chikungunya','chikun':'chikungunya','chiku':'chikungunya','chik':'chikungunya','chicungunya':'chikungunya','cesareo':'cesarea','cerebr':'cerebro','centralizar':'centralizacao','cefalicas':'cefalico','cefalicac':'cefalico','cefalica':'cefalico','cefalecina':'cefalexina','carniana':'cefalico','cardiopatia':'cardiaco','cardiop':'cardiaco','cardiaca':'cardiaco','calficicacoes':'calcificacao','calcificacoesreducao':'calcificacao','calcificacoe':'calcificacao','calcificaco':'calcificacao','calcifi':'calcificacao','calc':'calcificacao','cafalica':'cefalico','cabeca':'cefalico','cabecas':'cefalico','calcificacoes':'calcificacao','calcificar':'calcificacao','calsificacao':'calcificacao','capsular':'capsula','capsulo':'capsula','centrar':'centralizacao','cerebelar':'cerebelo','cerebelarcranio':'cerebelo','cerebrais':'cerebro','cerebral':'cerebro','cerebra':'cerebro', 'circunvolucao':'circunferencia', 'cistica':'cisto','cisticas':'cisto','cistico':'cisto','cistos':'cisto', 'compensataria':'compensatoria','conclusao':'confirmacao','confirmada':'confirmacao','confirmar':'confirmacao','cornar':'corneo','corno':'corneo','cornos':'corneo','corticais':'cortex','cortical':'cortex','corticos':'cortex','corporal':'corpo','craniana':'cranio','craniano':'cranio',
        'duplicidade':'duplo','doer':'dor','doen':'doenca','disturbios':'anormal','disponiveis':'disponivel','dilat':'crescimento','dignostico':'confirmacao','dignosticada':'confirmacao','diferente':'anormal','diarreico':'diarreia','diagnosticas':'diagnostico','diagnosticar':'diagnostico','diagnostica':'diagnostico','diagnostic':'diagnostico','diag':'diagnostico','detectavel':'deteccao','detectar':'deteccao','detec':'deteccao','destruicao':'anormal','desaparecer':'reducao','dengu':'dengue','deng':'dengue','degeneracao':'reducao','deformidade':'anormal','deformar':'anormal','deficit':'reducao','deficiencia':'reducao','dandy':'dandy-walker','dondy':'dandy-walker','walker':'dandy-walker','definidas':'confirmacao','definido':'confirmacao','destaca':'acentuada','determinando':'confirmacao','diametro':'circunferencia','diametros':'circunferencia','difusamente':'difusa','difusas':'difusa','difuso':'difusa','dilatar':'crescimento','dilatacao':'crescimento','dimensoes':'dimensao','diminuido':'reducao','diminuicao':'reducao','discreta':'discreto','discretamente':'discreto','dimorfismo':'dismorfismo','distribuidas':'distribuida','distribuir':'distribuida','delgado':'discreto','desproporcao':'anormal','dilatacao':'crescimento','diminuicao':'reducao','disproporcao':'anormal',
        'excessivo':'severo','exatema':'exantema','exantematima':'exantema','exantematico':'exantema','exantematicas':'exantema','exantematica':'exantema','evidencia':'confirmacao','etiologia':'etiologico','estreito':'discreto','estabelecido':'confirmacao','espont':'espontaneo','espalhar':'esparso','espaco':'esparso','epstein':'ebv','encefalico':'encefalo','ecograficos':'ecografico','ecografia':'ecografico','ecocardioigrama':'ecocardiograma','ecocardiog':'ecocardiograma','ecocardiagrama':'ecocardiograma','ecogenicidade':'ecogenico','elevar':'acentuada','encefalica':'encefalico','encefalo':'encefalico','esq':'esquerdo','esquer':'esquerdo','encefal':'encefalo','encefalico':'encefalo','enchimento':'crescimento','esparsas':'discreto','esquerda':'esquerdo','esquerdar':'esquerdo','estreitamento':'reducao',
        'fumar':'tabaco','fumante':'tabaco','fraco':'discreto','feto2':'fetal','feto1':'fetal','febril':'febre','febrel':'febre','familiar':'familia','falha':'anormal','fechamento':'fechar','fusao':'fechar','face':'facial','feto':'fetal','fissurar':'fissuras','focos':'foco','frontais':'frontal',
        'glicose':'glicemia','glic':'glicemia','gicemia':'glicemia','gestcao':'gestacao','gestacional':'gestacao','gestaca':'gestacao','gestac':'gestacao','gesta':'gestacao','gest':'gestacao','giros':'giro','giral':'giro','grosseiras':'grosseiro',
        'hsag':'hbs','hivs':'hiv','hipoxico':'hipoxia','hipotireioidismo':'hipotireoidismo','hipoplasicas':'hipoplasico','hipertesnao':'hipertensao','hipertenso':'hipertensao','hipertensivo':'hipertensao','hiperextensao':'crescimento','hiperestensao':'crescimento','heterogenea':'heterogeneo','herpes':'hsv','hepb':'hbs','hepatitec':'hcv','hepatiteb':'hbs','hepaptite':'hepatite','hemmorragia':'hemorragia','hemoglobia':'hemoglobina','hematrocrito':'hematocrito','hbc':'hcv','hbshg':'hbs','hbsg':'hbs','hbsag':'hbs','hbcv':'hcv','habitual':'comumente','hemisferios':'hemisferio','hemorragico':'hemorragia','hidroanencefalia':'hidrocefalia','hidranencefalia':'hidrocefalia','hiperecoicos':'hiperecoicas','hipodensa':'hipodensidade','hipoplasia':'reducao','holoprosecefalia':'holoprosencefalia',
        'irritabilida':'irritabilidade','irradiar':'esparso','intrautero':'intrauterino','intrauterinas':'intrauterino','intrauterina':'intrauterino','intracranianas':'intracraniana','intracerebral':'intracraniana','intercorrencias':'intercorrencia','intercorr':'intercorrencia','intenso':'severo','insuficiente':'reducao','insuficiencia':'reducao','infec':'infeccao','inespecificas':'inespecifico','indeterminar':'inderteminado','incomple':'incompleto','incomp':'incompleto','inchaco':'crescimento','implatacao':'implantacao','ilicitas':'ilicito','igm0':'igm','igg10':'igg','identificacao':'confirmacao','icterico':'ictericia','involucao':'reducao','inespecfico':'inespecifico','inespecificos':'inespecifico','inexpecifica':'inespecifico','infecciosa':'infeccao','infeccioso':'infeccao','injuria':'anormal','irregular':'anormal','interior':'interno','isquemica':'isquemico',
        'luxacao':'crescimento','linf':'linfocitos','leuco':'leucocito','leucocitos18':'leucocito','leucocitos':'leucocito','lesao':'anormal','lacerar':'anormal','laterais':'lateral','lisenfalia':'lisencefalia','later':'lateral','lados':'lateral','lineares':'linear','lisencefalias':'lisencefalia','lisencefalicas':'lisencefalia','linha':'linear','lobo':'lobos','lobolos':'lobos','localizar':'localizadas',
        'morfologico':'morfologia','mon':'monocitos','minimo':'reducao','microoftalmia':'microftalmia','microcelafia':'microcefalia','microcefali':'microcefalia','micr':'microcefalia','micro':'microcefalia','micricefalia':'microcefalia','microcalcificacao':'calcificacao','mental':'cognitivo','medicar':'medicamentar','medicamento':'medicamentar','medicacoes':'medicamentar','medicacao':'medicamentar','mediar':'medicacao','mediante':'medicacao','malformaca':'malformacao','malforma':'malformacao','malfor':'malformacao','malfomalcao':'malformacao','magnetico':'rm','magnetica':'rm','macrocalcificacoes':'calcificacao','microcalcificacoes':'calcificacao','microcefalico':'microcefalia','microcrania':'microcefalia','morfas':'morfologico','morfologica':'morfologico','multiplas':'variadas','multiplos':'variadas','multiplo':'variadas',
        'normalidade':'negativo','normalida':'negativo','normal':'negativo','norm':'negativo','nervosoatipico':'nervoso','nenhum':'negativo','negativar':'negativo','negati':'negativo','neg':'negativo','necessarios':'necessitar','necessario':'necessitar','nascido':'nascimento','nascer':'nascimento','nasc':'nascimento','nasal':'nariz','nuclear':'nucleo','nucleos':'nucleo',
        'ovalar':'oval','oligodramnia':'oligodramnio','oligamnio':'oligodramnio','ok':'negativo','oftamologica':'oftalmologia','oftalmologico':'oftalmologia','ocupitais':'occipital','occiptal':'occipital','obstetrico':'obstetrica','obstretica':'obstetrica','obstetri':'obstetrica','obstetra':'obstetrica','occipitais':'occipital','oligoamnio':'oligodramnio','oligodremnia':'oligodramnio',
        'plaq':'plaqueta','purido':'prurir','puerpera':'puerperio','puericultur':'puericultura','pruriginoso':'prurir','proteinas':'proteina','proseguir':'prosseguir','proliferar':'crescimento','presentar':'presenca','preenchimento':'preencher','possuir':'positivo','positivar':'positivo','pos':'positivo','polihidraminia':'polidramnio','persistencia':'persistente','perim':'perimetro','percetil':'percentil','patologico':'anormal','patologia':'anormal','parvo':'parvovirus','parequimatosas':'parenquima','parequima':'parenquima','parenqu':'parenquima','paremica':'parenquima','parametros':'padrao','parametro':'padrao','padr':'padrao','paquigirico':'paquigiria','parcialmente':'discreto','parcial':'discreto','paremquima':'parenquima','parenquimatosas':'parenquima','parenquimatoso':'parenquima','pariental':'parietal','pequenas':'discreto','periventricularaes':'periventricular','periventriculares':'periventricular','podend':'podendo','porcoes':'porcao','predominando':'acentuada','predominio':'acentuada','predominantemente':'acentuada','proeminencia':'acentuada','proeminente':'acentuada','perda':'ausencia','parietais':'parietal','pequena':'discreto','pequeno':'discreto','posteriores':'posterior',
        'quadruplo':'quadruplicar',
        'rinite':'alergico','rgico':'alergico','respiratorio':'respiracao','repetitivo':'repeticao','rubeolar':'rubeolar','rubeolaigm':'rubeola','rub':'rubeola','rubeol':'rubeola','rnm':'rm','rmm':'rm','restri':'restricao','ressonancia':'rm','resist':'resistencia','regante':'positivo','reg':'positivo','redu':'reducao','reativo':'positivo','realizdos':'realizar','realizacao':'realizar','realiz':'realizar','realiozados':'realizar','realiazados':'realizar','reagnete':'positivo','reagentetoxoplasmose':'toxo','reagenstes':'positivo','reagen':'positivo','reag':'positivo','rapidos':'rapido','radiar':'crescimento','reabsorcao':'reducao','regioes':'regiao','reduzir':'reducao','realizada':'realizar','realizou':'realizar','remanescente':'discreto',
        'suspeitar':'suspeito','significativo':'severo','suseptivel':'suscetivel','sucorticais':'subcortical','subcorticais':'subcortical','stoch':'storch','sorologicos':'sorologia','sorologico':'sorologia','sorologai':'sorologia','sorol':'sorologia','sonografico':'ultrasonografia','sonografias':'ultrasonografia','sisilis':'sifilis','sintomatologia':'sintoma','sindromica':'sindrome','sindrmoe':'sindrome','sinalizacao':'sinal','sifili':'sifilis','sifiles':'sifilis','sifiis':'sifilis','scaner':'scanner','sanguineo':'sangue','sinais':'sinal','segmento':'segmentar','seguimento':'segmentar','significativa':'severo','sequelar':'anormal','sequela':'anormal','simetrica':'simetrico','sulcos':'sulco','supratentarial':'supratentorial','supratentoreal':'supratentorial','supratentoriais':'supratentorial',
        'trasnsfontanela':'transfontanela','transfontonela':'transfontanela','transfontene':'transfontanela','transfontanelar':'transfontanela','transfontalena':'transfontanela','transfonta':'transfontanela','transfont':'transfontanela','transfon':'transfontanela','toxoplsmose':'toxo','toxoplasmpose':'toxo','toxoplasmose':'toxo','toxoplasmo':'toxo','toxoplasma':'toxo','toxoplasm':'toxo','toxoplamose':'toxo','toxopla':'toxo','toxiinfeccao':'toxo','tox':'toxo','torch':'storch','toracico':'torax','tomograficos':'tomografia','tomografico':'tomografia','tabagista':'tabaco','tabagismo':'tabaco','talamica':'talamo','talar':'talamo','tenue':'discreto','tenues':'discreto','temporais':'temporal','tentoriais':'temporal','torchs':'torch','torto':'anormal',
        'ustf':'transfontanela','ust':'transfontanela','usgtransfontonela':'transfontanela','usgtf':'transfontanela','usgt':'transfontanela','usgft':'transfontanela','usg':'ultrasonografia','usft':'transfontanela','usf':'ultrasonografia','ultrassons':'ultrasonografia','ultrassonograficos':'ultrasonografia','ultrassonografias':'ultrasonografia','ultrassonografia':'ultrasonografia','ultrassonog':'ultrasonografia','ultrassongrafia':'ultrasonografia','ultrasson':'ultrasonografia','ultrassom':'ultrasonografia','ultrasso':'ultrasonografia','ultrasonografias':'ultrasonografia','ultrasom':'ultrasonografia','ultras':'ultrasonografia',
        'virose':'virus','viral':'virus','ventroculomegalia':'ventriculomegalia','ventriculomagalia':'ventriculomegalia','vasoculopatia':'vasculopatia','variar':'variadas','varginal':'vagina','vaginal':'vagina','vacinal':'vacinar','variante':'variadas','ventricomegalia':'ventriculomegalia','ventricular':'ventriculo','ventriculos':'ventriculo','venix':'vermix','vermis':'vermix','vernix':'vermix','vasculopatias':'vasoculopatia','ventriculomagele':'ventroculomegalia','ventriculomegalia':'ventroculomegalia','ventricumegalia':'ventroculomegalia','ventriculomegalia':'ventroculomegalia','ventroculomegalia':'ventriculomegalia','volumar':'volume','volumetrica':'volume','volumetrico':'volume',
        'walter':'dandy-walker',
        'zikavirus':'zika','zica':'zika','zi':'zika'
        }


nlp = spacy.load("pt_core_news_sm")
ponto = string.punctuation
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
stopPalavras = [similar(word,mapa) for word in stopPalavras]
#select words 
text =text.tolist()       
docs_total= []
lista_total = []
#     col = XDf.columns
#     #XDf = MinMaxScaler().fit_transform(XDf)
#     XDf=pd.DataFrame(XDf)
#     XDf.columns = col
for t in text:
    tokens, doc = extrair(t,mapa,ponto)
    docs_total.append(doc)
    lista_total.append(tokens.copy())
del doc
del t
var_total = []
for tokens in lista_total:
         for p in tokens:
             if p not in var_total:
                 var_total.append(p)    
# salvar palavras
file = open('words.txt','w')
# add words var
for w in var_total:
    file.write(w+'\n')
file.close()
del w
del tokens
del p
for var in var_total:
    tam = len(X)
    lvar = np.zeros(tam,dtype='int64')
    for i in range(tam):
        if var in lista_total[i]:
            lvar[i] = 1
        else:
            lvar[i] = 0
    aux=var+'_word'
    X[aux] = lvar
X=X.astype('int64')
#gerate model
modelo_total = GradientBoostingClassifier(max_depth=8,min_samples_split=5,random_state=seed)
modelo_total.fit(X,Y)
#save model
file = open('classific2.dat','wb')
pk.dump(modelo_total,file)
file.close()
#save result
ypred = modelo_total.predict(X)
ypred =pd.Series(ypred)
ypred.replace([0,1,2,3],['Discarded','Somewhat probable','Moderately probable','Highly probable'],inplace=True)

XDf.loc[XDf.typeClass=='group2','classFinal'] =  list(ypred)
XDf.to_csv('banco_total3.csv')  
#save data
file = open('stopwords.dat','wb')
pk.dump(stopPalavras,file)
file.close()
file = open('mapa.dat','wb')
pk.dump(mapa,file)
file.close()