# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/23
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：Adult_Processing.py
@IDE ：PyCharm
"""
from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

# fetch dataset
adult = fetch_ucirepo(id=2)
# metadata
print(adult.metadata)
# variable information
print(adult.variables)

# data (as pandas dataframes)
X = adult.data.features
y = adult.data.targets

# initial data
df = pd.concat([X, y], axis=1)
df.drop(['education-num'], axis=1, inplace=True)
df.head()
df.info()

# update missing value and label value
df.replace("?", pd.NaT, inplace= True)
df.replace(">.+", "1", regex= True, inplace= True)
df.replace("<=.+", "0", regex= True, inplace= True)
# insert mode
trans = {'workclass': df['workclass'].mode()[0], 'occupation': df['occupation'].mode()[0], 'native-country' : df['native-country'].mode()[0]}
df.fillna(trans, inplace = True)

# classification attribute columns in training data
object_cols = [col for col in df.columns if df[col].dtype == "object"]

# apply ordinal encoder
my_ordinalEncoder = OrdinalEncoder()
df[object_cols] = my_ordinalEncoder.fit_transform(df[object_cols])
df.head()
df.info()

# check results
# for col in object_cols:
#     print(max(df[col]))

# save the data as csv file
df.to_csv("Adult.csv", index=False)




