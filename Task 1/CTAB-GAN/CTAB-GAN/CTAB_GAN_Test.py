# -*- coding: utf-8 -*-
"""
@Time ： 2024/11/23
@Auth ： Chuang Liu
@Email ：LIUC0316@126.COM
@File ：CTAB_GAN_Test
@IDE ：PyCharm
"""

# Importing the model
from model.ctabgan import CTABGAN
# Importing the evaluation metrics
from model.eval.evaluation import get_utility_metrics,stat_sim,privacy_metrics
# Importing standard libraries
import numpy as np
import pandas as pd
import glob

# Specifying the replication number
num_exp = 1
# Specifying the name of the dataset used
dataset = "Adult"
# Specifying the path of the dataset used
real_path = "Real_Datasets/Adult/Adult.csv"
# Specifying the root directory for storing generated data
fake_file_root = "Fake_Datasets"

# Initializing the synthesizer object and specifying input parameters
# Notice: If you have continuous variable, you do not need to explicitly assign it. It will be treated like
# that by default
synthesizer =  CTABGAN(raw_csv_path = real_path,
                 test_ratio = 0.20,
                 categorical_columns = ['workclass', 'education', 'marital-status', 'occupation',
                                        'relationship', 'race', 'gender', 'native-country', 'income'],
                 log_columns = [],
                 mixed_columns= {'capital-loss':[0.0],'capital-gain':[0.0]},
                 integer_columns = ['age', 'fnlwgt','capital-gain', 'capital-loss','hours-per-week'],
                 problem_type= {"Classification": 'income'},
                 epochs = 150)

# Fitting the synthesizer to the training dataset and generating synthetic data
for i in range(num_exp):
    synthesizer.fit()
    syn = synthesizer.generate_samples()
    syn.to_csv(fake_file_root+"/"+dataset+"/"+ dataset+"_fake_{exp}.csv".format(exp=i), index= False)

# Collecting the paths to all corresponding generated datasets for evaluation
fake_paths = glob.glob(fake_file_root+"/"+dataset+"/"+"*")

# Specifying the list of classifiers to conduct ML utility evaluation
classifiers_list = ["lr","dt","rf","mlp","svm"]

# Storing and presenting the results as a dataframe
result_mat = get_utility_metrics(real_path,fake_paths,"MinMax",classifiers_list, test_ratio = 0.20)
result_df  = pd.DataFrame(result_mat,columns=["Acc","AUC","F1_Score"])
result_df.index = classifiers_list

# Specifying the categorical columns of the dataset used
adult_categorical = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country', 'income']

# Storing and presenting the results as a dataframe
stat_res_avg = []
for fake_path in fake_paths:
    stat_res = stat_sim(real_path,fake_path,adult_categorical)
    stat_res_avg.append(stat_res)

stat_columns = ["Average WD (Continuous Columns","Average JSD (Categorical Columns)","Correlation Distance"]
stat_results = pd.DataFrame(np.array(stat_res_avg).mean(axis=0).reshape(1,3),columns=stat_columns)

# Storing and presenting the results as a dataframe
priv_res_avg = []
for fake_path in fake_paths:
    priv_res = privacy_metrics(real_path, fake_path)
    priv_res_avg.append(priv_res)

privacy_columns = ["DCR between Real and Fake (5th perc)", "DCR within Real(5th perc)", "DCR within Fake (5th perc)",
                   "NNDR between Real and Fake (5th perc)", "NNDR within Real (5th perc)",
                   "NNDR within Fake (5th perc)"]
privacy_results = pd.DataFrame(np.array(priv_res_avg).mean(axis=0).reshape(1, 6), columns=privacy_columns)

# Storing generated data for future use if needed
syn.to_csv(fake_file_root+"/"+dataset+"/"+ dataset+"_fake_{exp}.csv".format(exp=i), index= False)
