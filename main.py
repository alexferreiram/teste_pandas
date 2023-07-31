# -*- coding: utf-8 -*-
# @Author  : Alex Ferreira
# @Email   : alex.ferreiram@ufpe.br
# @File    : main.py
# @Software: PyCharm

import pandas as pd

# datframe_pd = pd.read_csv("coloncancer.txt", delim_whitespace=True)
# a = datframe_pd.describe()
# print(datframe_pd)

demanda = dict()
demanda['subsistema'] = list()
demanda['semihora'] = list()
demanda['MW'] = list()

pequsinas = dict()
pequsinas['subsistema'] = list()
pequsinas['semihora'] = list()
pequsinas['Eolic'] = list()
pequsinas['Hidra'] = list()
pequsinas['Solar'] = list()
pequsinas['Termi'] = list()
pulo = 0 # 30*2 variável add para ler outros dias

dadosrede = dict()
dadosrede["Patamar"] = list()
dadosrede["NuBar"] = list()
dadosrede["Status"] = list()
dadosrede["subsistema"] = list()
dadosrede["Area"] = list()
dadosrede["MW"] = list()

# leitura prev carga
arq1 = open("arqcargaprev.txt", "r")
s = arq1.readline()

while s[:5] != "TEMPO":
    if s[:2] in (" 1", " 2", " 3", " 4"):
        demanda['subsistema'].append(int(s[:3]))
        demanda['semihora'].append(int(s[3:6]))
        demanda['MW'].append(int(s[8:15]))
    s = arq1.readline()
    # elif s[:51] =="--------------------------------------------------"
arq1.close()

# leitura pequenas usinas
arq2 = open("arqpequsinas.txt", "r")
r = arq2.readline()

while r[:5] != "TEMPO":
    if r[:2] in (" 1", " 2", " 3", " 4"):
        pequsinas['subsistema'].append(int(r[:3]))
        pequsinas['semihora'].append(int(r[3:6]))
        pequsinas['Eolic'].append(int(r[6+pulo:12+pulo]))
        pequsinas['Hidra'].append(int(r[12+pulo:18+pulo]))
        pequsinas['Solar'].append(int(r[18+pulo:24+pulo]))
        pequsinas['Termi'].append(int(r[24+pulo:30+pulo]))
    r = arq2.readline()
arq2.close()

# leitura dados rede
arq3 = open("arqdadosrede.txt","r")
t = arq3.readline()
contador = 0

while contador <= 1:
    if t[:3] == "---":
        contador += 1
    elif t[:3] == "ONS":
        patamar = t[22:27]
    else:
        dadosrede["Patamar"].append(patamar)
        dadosrede["NuBar"].append(int(t[:6]))
        dadosrede["Status"].append(t[6])
        dadosrede["subsistema"].append(int(t[29]))
        dadosrede["Area"].append(int(t[22:26]))
        dadosrede["MW"].append((float(t[39:45])))
    t = arq3.readline()
arq3.close()

df_cargaprev = pd.DataFrame(demanda)
df_gerpequsi = pd.DataFrame(pequsinas)
df_dadosrede = pd.DataFrame(dadosrede)

print("teste")