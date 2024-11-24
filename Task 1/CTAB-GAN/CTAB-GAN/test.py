# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/24
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：test
@IDE ：PyCharm
"""
import pandas as pd

data = pd.read_csv('Real_Datasets/Adult.csv')
data.info()
data = data.infer_objects()
data.info()

print(data)
