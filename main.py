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

arq = open("arqcargaprev.txt", "r")
s = arq.readline()


while s[:5] != "TEMPO":
    if s[:2] in (" 1", " 2", " 3", " 4"):
        demanda['subsistema'].append(int(s[:3]))
        demanda['semihora'].append(int(s[3:6]))
        demanda['MW'].append(int(s[8:15]))
    s = arq.readline()
    # elif s[:51] =="--------------------------------------------------"

df_cargaprev = pd.DataFrame(demanda)
arq.close()
print("teste")