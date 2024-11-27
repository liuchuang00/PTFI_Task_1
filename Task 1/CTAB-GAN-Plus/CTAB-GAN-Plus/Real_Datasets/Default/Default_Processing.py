# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/26
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：Default_Processing
@IDE ：PyCharm
"""

import pandas as pd

# read excel file
df = pd.read_excel('default of credit card clients.xls',skiprows=1)
# Remove unwanted feature
df.drop('ID',axis=1,inplace=True)
df.head()
df.info()

# save csv file
df.to_csv("Default.csv",index=False)



