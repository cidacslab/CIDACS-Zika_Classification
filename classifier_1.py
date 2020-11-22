# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 08:15:03 2020

@author: rafae
"""

import pandas as pd
import numpy as np
import pickle as pk
from sklearn.ensemble import RandomForestClassifier


seed = 1234
XDf = pd.read_csv("banco_total.csv",index_col=0)
X = XDf[XDf.typeClass=="group1"].copy()
del X['texto']
X.sexo.replace(['Feminino','Masculino'],[0,1],inplace=True)  
X =X.fillna(-9)
X.iloc[:,2:19] = X.iloc[:,2:19].astype('object')
X.sexo = X.sexo.astype('int64')
X['sexo_miss'] = X['sexo'].copy()
X.sexo_miss.replace([1,0,-9],[0,0,1],inplace=True)
X.sexo.replace([-9],[0],inplace=True)
X['tamanhoCabe_miss'] = X['tamanhoCabe'].copy()
X.loc[X.tamanhoCabe!=-9,'tamanhoCabe_miss'] = 0 
X.tamanhoCabe_miss.replace([-9],[1],inplace=True) 
X.tamanhoCabe.replace([-9],[32],inplace=True)  
X['classFeto_miss'] = X.classFeto.copy()
X.classFeto.replace(['Termo','Pré-Termo','Pós-Termo',-9],[1,0,2,0],inplace=True)   
X.loc[X.classFeto_miss!=-9,'classFeto_miss'] =0  
X.loc[X.classFeto_miss==-9,'classFeto_miss'] =1  
X["micro_miss"] = X.micro.copy()
X.micro.replace([-9],[0])
X.loc[X.micro_miss!=-9,'micro_miss']=0
X.loc[X.micro_miss==-9,'micro_miss']=1
del X['NV_TC_MICRO']
del X['NV_Storch']
del X['NV_sifilis']  
del X['count_storch']     
del X['NV_TOXO']   
del X['NV_CMV']
del X['NV_DENGUE']
del X['NV_CHIK']
del X['NV_USG_MICRO']
del X['NV_RM_MICRO']
del X['NV_USG_RESULT']
del X['NV_TC_RESULT']
del X['NV_RM_RESULT']
del X['missImagem']
Y = X.casegr.copy()  
del X['casegr']
del X['typeClass']
del X['classFinal']
Y.replace(['Discarded','Somewhat probable'],[0,1],inplace=True)
X = X[['sexo','sexo_miss','tamanhoCabe','tamanhoCabe_miss','classFeto','classFeto_miss','micro','micro_miss']]
#create classify
modelo_RF = RandomForestClassifier(min_samples_split=40,max_depth=5,random_state=seed)
modelo_RF.fit(X,Y) 
#save classify
file = open('classific1.dat','wb')
pk.dump(modelo_RF,file)
file.close()
#save X and Y
file = open('Xclassific1.dat','wb')
pk.dump(X,file)
file.close()
file = open('Yclassific1.dat','wb')
pk.dump(Y,file)
file.close()
ypred = modelo_RF.predict(X)
ypred =pd.Series(ypred)
ypred.replace([0,1],['Discarded','Somewhat probable'],inplace=True)

XDf.loc[XDf.typeClass=='group1','classFinal'] =  list(ypred)
XDf.to_csv('banco_total2.csv')  
