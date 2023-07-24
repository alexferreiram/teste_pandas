# -*- coding: utf-8 -*-
# @Author  : Alex Ferreira
# @Email   : alex.ferreiram@ufpe.br
# @File    : main.py
# @Software: PyCharm

import pandas as pd

datframe_pd = pd.read_csv("arqcargaprev.txt", delim_whitespace=True)
a = datframe_pd.describe()
print(datframe_pd)