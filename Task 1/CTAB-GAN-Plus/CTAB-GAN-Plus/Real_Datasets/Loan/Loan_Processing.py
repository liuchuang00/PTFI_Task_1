# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/24
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：Loan_Processing
@IDE ：PyCharm
"""

# only for Python 3.10+
# import mlcroissant as mlc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import normaltest

# # Fetch the Croissant JSON-LD
# croissant_dataset = mlc.Dataset('www.kaggle.com/datasets/itsmesunil/bank-loan-modelling/croissant/download')
#
# # Check what record sets are in the dataset
# record_sets = croissant_dataset.metadata.record_sets
# print(record_sets)
#
# # Fetch the records and put them in a DataFrame
# record_set_df = pd.DataFrame(croissant_dataset.records(record_set=record_sets[0].uuid))
# record_set_df.head()

# input kaggle datasets download itsmesunil/bank-loan-modelling to the terminal to get .xlsx
df = pd.read_excel("../Bank_Personal_Loan_Modelling.xlsx", sheet_name='Data')
df.drop(['ID'], axis=1, inplace=True)
df.head()
df.info()

# make label Personal Loan be the last column
col_a = df.columns.get_loc("Personal Loan")
col_b = df.columns.get_loc("CreditCard")
df_copy = df.copy()
list_cols = df_copy.columns.tolist()
list_cols[col_a], list_cols[col_b] = list_cols[col_b], list_cols[col_a]
df = df_copy.reindex(columns=list_cols)
df.head()
df.info()
df.to_csv("Loan.csv", index=False)

# check whether each variable follows a Gaussian distribution and visualize it
for column in df.columns:
    # perform a normality test
    stat, p_value = normaltest(df[column])
    print(f'Column: {column}, Normality Test p-value: {p_value}')
    if p_value > 0.05:
        print(f'{column} may follow Gaussian distribution')
    else:
        print(f'{column} do not follow Gaussian distribution')

    # visual distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, color='blue')
    plt.title(f'Distribution of {column}')
    plt.show()

