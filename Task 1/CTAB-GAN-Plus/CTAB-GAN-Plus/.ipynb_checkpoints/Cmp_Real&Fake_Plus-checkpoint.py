# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/25
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：Cmp_Real&Fake_Plus
@IDE ：PyCharm
"""

import pandas as pd
from table_evaluator import TableEvaluator
import glob

fake_file_root = "Fake_Datasets"
real_file_root = "Real_Datasets"
dataset = "Loan"
fake_paths = glob.glob(fake_file_root+"/"+dataset+"/"+"*")
Real_Dataset = pd.read_csv(real_file_root + '/' + dataset + '/' + dataset + '.csv')
Fake_Dataset = pd.read_csv(fake_paths[0])
Real_Dataset.head()
Real_Dataset.info()
Fake_Dataset.head()
Fake_Dataset.info()

print(Real_Dataset.shape, Fake_Dataset.shape)
table_evaluator = TableEvaluator(Real_Dataset, Fake_Dataset)

table_evaluator.visual_evaluation()