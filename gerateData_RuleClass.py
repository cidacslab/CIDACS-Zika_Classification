# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 08:49:21 2020

@author: rafae
"""

import pandas as pd
import numpy as np



def gerarbanco():
    banco = pd.read_stata("Microcefalia MS analysis 20160609.dta")
    circ = pd.read_csv("circumference.csv",sep=";",index_col='sem') 
    banco.index = range(len(banco.index))
    bancoNovo = pd.DataFrame()
    banco.NV_USG_RESULT.replace( ['ALTERADO','NORMAL'],['Alterado','Normal'],inplace=True)
    # rule classification
    sexo = banco.TP_SEXO
    classFinal = pd.Series([np.nan]*len(sexo))
    classFinal[banco.NV_CMV=='IgM reagente'] = 'Discarded'
    classFinal[banco.NV_HCV=='Reagente'] = 'Discarded'
    classFinal[banco.NV_RUBEOLA=='IgM reagente'] = 'Discarded'
    classFinal[banco.NV_TOXO=='IgM reagente'] = 'Discarded'
    classFinal[banco.NV_RM_RESULT=='Normal'] = 'Discarded'
    classFinal[banco.NV_TC_RESULT=='Normal'] = 'Discarded'
    

    classFinal[banco.NV_ZIKA=='Positivo'] = 'Definite'
    
    # organize database
    tamanhoCabe = banco.headcirc
    
    bancoNovo['sexo'] = list(sexo)
    bancoNovo['tamanhoCabe'] = list(tamanhoCabe)
    bancoNovo['classFeto'] = list(banco.TP_CLASSIFICACAO_FETO_RN)
    semanaGes = banco.SINASC_SEMAGESTAC
    missing = pd.Series([np.nan]*len(sexo))
    missing[bancoNovo.tamanhoCabe.isnull()]=1
    missing[sexo.isnull()]=1
    missing[bancoNovo.classFeto.isnull()]=1
    missing[semanaGes.isnull()]=1
    micro = pd.Series([np.nan]*len(sexo))
    for i in range(len(sexo)):
        if missing[i]!=1:
            if semanaGes[i]<=42 and semanaGes[i]>=14:
                
                ref1 =0
                if sexo[i]=='Masculino':
                    ref1 = circ.boy_min[semanaGes[i]]
                else:
                    ref1 = circ.girl_min[semanaGes[i]]
                if tamanhoCabe[i]<ref1:
                    micro[i]=1
                else:
                    micro[i]=0
    bancoNovo['micro'] = list(micro)
    banco['micro']=micro
    bancoNovo['NV_TC_MICRO'] = list(banco.NV_TC_MICRO)
    
    
    #sorologia
    bancoNovo['NV_Storch'] =list(banco.lab_STORCH)
    bancoNovo['NV_sifilis'] = list(banco.NV_SIFILIS)
    bancoNovo['NV_TOXO'] = list(banco.NV_TOXO.replace(['IgG reagente','IgM reagente'],['Reagente','Reagente']))
    bancoNovo['NV_CMV'] =list( banco.NV_CMV)
    bancoNovo['NV_DENGUE']=list(banco.NV_DENGUE.replace(['IgG reagente','IgM reagente'],['Reagente','Reagente']))
    bancoNovo['NV_CHIK']=list(banco.NV_CHIK)
    
    count_storch = pd.Series([np.nan]*len(sexo))
    for i in range(len(sexo)):
            if len(bancoNovo.NV_sifilis[i].strip())>1:
                count_storch[i]=1
            if len(bancoNovo.NV_CMV[i].strip())>1:
                if count_storch.isnull()[i]:
                    count_storch[i]=1
                else:
                    count_storch[i]=count_storch[i]+1
            if len(bancoNovo.NV_TOXO[i].strip())>1:
                if count_storch.isnull()[i]:
                    count_storch[i]=1
                else:
                    count_storch[i]=count_storch[i]+1
            
    banco['count_storch'] = count_storch
    bancoNovo['count_storch'] = list(count_storch)
    #exames
    bancoNovo['NV_USG_MICRO']=list(banco.NV_USG_MICRO)
    bancoNovo['NV_TC_MICRO']=list(banco.NV_TC_MICRO)
    bancoNovo['NV_RM_MICRO']=list(banco.NV_RM_MICRO)
    bancoNovo['NV_USG_RESULT']=list(banco.NV_USG_RESULT)
    bancoNovo['NV_TC_RESULT']=list(banco.NV_TC_RESULT)
    bancoNovo['NV_RM_RESULT']=list(banco.NV_TC_RESULT)
   
    
    
    texto = banco.NV_RM_CALC
    texto = texto + ' ' + banco.NV_USG_CALC_DESC  
    texto = texto + ' ' + banco.NV_RM_CALC
    texto = texto + ' ' + banco.NV_TC_CALC
    texto = texto + ' ' + banco.NV_USG_OUTRO
    texto = texto + ' ' + banco.NV_TC_OUTRO
    texto = texto + ' ' + banco.NV_RM_OUTRO
    texto = texto + ' ' + banco.NV_USG_VENTR
    texto = texto + ' ' + banco.NV_TC_VENTR
    texto = texto + ' ' + banco.NV_RM_VENTR
    
    
    
    missImagem = pd.Series([np.nan]*len(sexo))
    for i in range(len(sexo)):
        if len(banco.NV_USG_RESULT[i].strip())<2 and len(banco.NV_TC_RESULT[i].strip())<2 and len(banco.NV_RM_RESULT[i].strip())<2 and len(texto[i].strip())<2:
            missImagem[i] = 1
        else:
            missImagem[i] = 0
        
    texto = texto + ' ' + banco.DS_OBSERVACOES_GERAIS
    
    for i in range(len(texto)):
        texto[i] = texto[i].strip().replace('.',' ').replace(';',' ').replace(',',' ').replace('?',' ').replace("'",' ').replace('=','').replace('-',' ').replace('+',' ').replace('/',' ').replace('(',' ').replace(')',' ').replace('<',' ').replace('>',' ').replace(':',' ').replace('&',' ').replace('¿',' ').replace('%',' ').replace('\n',' ').replace('"',' ').lower()
    
    bancoNovo['missImagem'] = list(missImagem)
    bancoNovo['casegr'] = list(banco.casegr)
    bancoNovo['classFinal']=list(classFinal)
    return texto,bancoNovo
    
texto,bancoNovo = gerarbanco()
bancoNovo['texto'] = list(texto)


# type class and save
typeClass= pd.Series([np.nan]*len(bancoNovo))
typeClass[bancoNovo.classFinal.isnull()==False]='rule'
typeClass[(typeClass.isnull()) & (bancoNovo.texto.str.strip()!='')]='group2'
typeClass[typeClass.isnull()]='group1'
bancoNovo['typeClass']=list(typeClass)

bancoNovo.to_csv('banco_total.csv')