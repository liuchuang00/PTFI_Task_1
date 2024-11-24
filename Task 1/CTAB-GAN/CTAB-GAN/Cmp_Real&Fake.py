# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/23
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：Cmp_Real&Fake
@IDE ：PyCharm
"""
import pandas as pd
from table_evaluator import TableEvaluator

Real_Dataset = pd.read_csv('Real_Datasets/Adult/Adult.csv')
Fake_Dataset = pd.read_csv('Fake_Datasets/Adult/Adult_fake_0.csv')

Real_Dataset.head()
Real_Dataset.info()
Fake_Dataset.head()
Fake_Dataset.info()

print(Real_Dataset.shape, Fake_Dataset.shape)
categorical_columns = ['workclass', 'education', 'marital-status', 'occupation',
                                        'relationship', 'race', 'sex', 'native-country', 'income']
table_evaluator = TableEvaluator(Real_Dataset, Fake_Dataset, cat_cols=categorical_columns)

table_evaluator.visual_evaluation()
