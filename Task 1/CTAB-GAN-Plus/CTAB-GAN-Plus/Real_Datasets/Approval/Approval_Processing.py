# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/26
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：Approval_Processing
@IDE ：PyCharm
"""

import pandas as pd

# read excel file
df_columns = ['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','T1']
df = pd.read_csv('australian.dat', sep=' ', names=df_columns)
df.head()
df.info()

# save csv file
df.to_csv("Approval.csv",index=False)