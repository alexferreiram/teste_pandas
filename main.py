# -*- coding: utf-8 -*-
# @Author  : Alex Ferreira
# @Email   : alex.ferreiram@ufpe.br
# @File    : main.py
# @Software: PyCharm

import pandas as pd

def LeituraDados(): #função que realiza a leitura dos dados p posteriormente transf em dataframe
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
            rede_Leve["Patamar"].append(patamar)
            rede_Leve["NuBar"].append(int(t[:6]))
            rede_Leve["Status"].append(t[6])
            rede_Leve["subsistema"].append(int(t[29]))
            rede_Leve["Area"].append(int(t[22:26]))
            rede_Leve["MW"].append((float(t[39:45])))
        t = arq3.readline()
    arq3.close()

    # leitura danc
    arq4 = open("AreaDANC.txt", "r")
    u = arq4.readline()
    contador = 0

    while u[:5] != "TEMPO":
        if u[:4] == "----" or u[:4] == "AREA":
            u = arq4.readline()
            continue
        # elif u[:4] == :
        #     u = arq4.readline()
            # continue
        else:
            a = 5
            for i in range(1, 49):
                b = a + 6
                danc[f"Pat{i:02d}"].append(u[a:b])
                a = b + 1
            danc["Area"].append(int(u[:4]))
            u = arq4.readline()
    arq4.close()
    # entender o motivo pelo qual os dataframes não são criados quando dentro da funcao
    #df_cargaprev = pd.DataFrame(demanda)
    #df_gerpequsi = pd.DataFrame(pequsinas)
    #df_rede_Leve = pd.DataFrame(rede_Leve)
    #df_danc = pd.DataFrame(danc)


    # eliminar áreas com DANC 0.00
    #df_danc = df_danc[df_danc["Pat01"] != '  0.00']

    return [demanda,pequsinas,rede_Leve,danc] #função qu $

# criando dicionário demanda
demanda = {
 'subsistema': [], 'semihora': [], 'MW': []
}

# criando dicionário pequsinas
pequsinas = {
 'subsistema': [], 'semihora': [], 'Eolic': [], 'Hidra': [], 'Solar': [], 'Termi': []
}
pulo = 0 # 30*2 variável add para ler outros dias

# criando dicionário rede_Leve
rede_Leve = {
 "Patamar": [], "NuBar": [], "Status": [], "subsistema": [], "Area": [], "MW": []
}

# criando dicionário danc
danc = {
        "Area": [],
        "Pat01": [], "Pat02": [], "Pat03": [], "Pat04": [], "Pat05": [],
        "Pat06": [], "Pat07": [], "Pat08": [], "Pat09": [], "Pat10": [],
        "Pat11": [], "Pat12": [], "Pat13": [], "Pat14": [], "Pat15": [],
        "Pat16": [], "Pat17": [], "Pat18": [], "Pat19": [], "Pat20": [],
        "Pat21": [], "Pat22": [], "Pat23": [], "Pat24": [], "Pat25": [],
        "Pat26": [], "Pat27": [], "Pat28": [], "Pat29": [], "Pat30": [],
        "Pat31": [], "Pat32": [], "Pat33": [], "Pat34": [], "Pat35": [],
        "Pat36": [], "Pat37": [], "Pat38": [], "Pat39": [], "Pat40": [],
        "Pat41": [], "Pat42": [], "Pat43": [], "Pat44": [], "Pat45": [],
        "Pat46": [], "Pat47": [], "Pat48": []
    }
print("ola")

LeituraDados()

# criando dataframes
df_cargaprev = pd.DataFrame(demanda)
df_gerpequsi = pd.DataFrame(pequsinas)
df_rede_Leve = pd.DataFrame(rede_Leve)
df_danc = pd.DataFrame(danc)

# eliminar áreas com DANC 0.00
df_danc = df_danc[df_danc["Pat01"] != '  0.00']

df_soma_por_area = df_rede_Leve.groupby('Area')['MW'].sum().reset_index()
df_soma_por_subs = df_rede_Leve.groupby('subsistema')['MW'].sum().reset_index()
soma_por_subs = df_soma_por_subs.values.tolist()


# -------------  Fim leitura dados do txt
# Metodologia


print("teste")