# PTFI_Task_1
## Introduction
This is the solution for the financial dataset generation task of Privacy Technologies for Financial Intelligence (PTFI[1]), which is a Data Bytes Company project and available in https://github.com/DataBytes-Organisation/Privacy-Technologies-for-Financial-Intelligence. The specific task plan is shown in the following document:
- [Synthetic_Data_Analysis_2nd.pdf](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Synthetic%20Data%20Analysis_2nd.pdf)


## Structure
***1. Dataset Processing and Presentation***  
We processed four datasets (Approval[2], Default[3], Loan[4], and Adult[5]) in our local programs on Pycharm. The specific operations include filling in missing values, correcting incorrect values and saving them as .csv files. The local programs are as follows:   
  - [Approval_Processing.py](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Approval/Approval_Processing.py)
  - [Default_Processing.py](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Default/Default_Processing.py)
  - [Loan_Processing.py](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Loan/Loan_Processing.py)
  - [Adult_Processing.py](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Adult/Adult_Processing.py)     

At the same time, we use notebooks on Jupyter to show not only the process of the above local programs, but also some mathematical properties of the datasets. The specific notebooks are as follows:
  - [Approval_Processing.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Approval/Approval_Processing.ipynb)
  - [Default_Processing.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Default/Default_Processing.ipynb)
  - [Loan_Processing.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Loan/Loan_Processing.ipynb)
  - [Adult_Processing.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Adult/Adult_Processing.ipynb)  

***2. Models and Data Generation Presentation***    
We selecte two generative network models CTAB-GAN[6] and CTAB-GAN+[7] for this task. The specific models and related articles are as follows:    
  - [CTAB-GAN](https://github.com/liuchuang00/PTFI_Task_1/tree/master/Task%201/CTAB-GAN/CTAB-GAN/model)
  - [CTAB-GAN+](https://github.com/liuchuang00/PTFI_Task_1/tree/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/model)
  - [CTAB-GAN_Effective_Table_Data_Synthesizing.pdf](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN_Effective_Table_Data_Synthesizing.pdf)
  - [CTAB-GAN+_enhancing_tabular_data_synthesis.pdf](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN%2B_enhancing_tabular_data_synthesis.pdf)    

We use the above two models to simulate data generation for all four datasets. The results are visualized with notebooks. The specific process of CTAB-GAN can be found in the following notebooks:    
  - [Approval_Mocking.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Approval_Mocking.ipynb)
  - [Default_Mocking.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Default_Mocking.ipynb)
  - [Loan_Mocking.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Loan_Mocking.ipynb)
  - [Adult_Mocking.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Adult_Mocking.ipynb)    

The specific process of CTAB-GAN+ can be found in the following notebooks:  
  - [Approval_Mocking_Plus.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Approval_Mocking_Plus.ipynb)
  - [Default_Mocking_Plus.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Default_Mocking_Plus.ipynb)
  - [Loan_Mocking_Plus.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Loan_Mocking_Plus.ipynb)
  - [Adult_Mocking_Plus.ipynb](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Adult_Mocking_Plus.ipynb)

***3. Real and Fake datasets***    
The four real datasets are as follows:  
  - [Approval.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Approval/Approval.csv)
  - [Default.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Default/Default.csv)
  - [Loan.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Loan/Loan.csv)
  - [Adult.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Real_Datasets/Adult/Adult.csv)   

The four fake datasets from CTAB-GAN are as follows:
  - [Approval_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Fake_Datasets/Approval/Approval_fake_0.csv)
  - [Default_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Fake_Datasets/Default/Default_fake_0.csv)
  - [Loan_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Fake_Datasets/Loan/Loan_fake_0.csv)
  - [Adult_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Fake_Datasets/Adult/Adult_fake_0.csv)   

The four fake datasets from CTAB-GAN+ are as follows:
  - [Approval_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Fake_Datasets/Approval/Approval_fake_0.csv)
  - [Default_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Fake_Datasets/Default/Default_fake_0.csv)
  - [Loan_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Fake_Datasets/Loan/Loan_fake_0.csv)
  - [Adult_fake_0.csv](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Fake_Datasets/Adult/Adult_fake_0.csv)

***4. Test programs***   
There are some trial files like the following:  
  - [CTAB_GAN_Test.py](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/CTAB_GAN_Test.py)
  - [Cmp_Real&Fake.py](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN/CTAB-GAN/Cmp_Real%26Fake.py)
  - [Cmp_Real&Fake_Plus.py](https://github.com/liuchuang00/PTFI_Task_1/blob/master/Task%201/CTAB-GAN-Plus/CTAB-GAN-Plus/Cmp_Real%26Fake_Plus.py)

## Reference
[1] PTFI (2024). Privacy-Technologies-for-Financial-Intelligence [Website]. Github Repository. Available: https://github.com/DataBytes-Organisation/Privacy-Technologies-for-Financial-Intelligence.   
[2] R. Quinlan (1987). Statlog (Australian Credit Approval) [Dataset]. UCI Machine Learning Repository. Available: http://archive.ics.uci.edu/dataset/143/statlog+australian+credit+approval.  
[3] I. Yeh (2009). Default of Credit Card Clients [Dataset]. UCI Machine Learning Repository. Available: http://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients.  
[4] Sunil Jacob (2024). Bank_Loan_modelling [Dataset]. Kaggle Repository. Available: https://www.kaggle.com/datasets/itsmesunil/bank-loan-modelling/data.  
[5] B. Becker and R. Kohavi (1996). Adult [Dataset]. UCI Machine Learning Repository. Available: https://archive.ics.uci.edu/dataset/2/adult.      
[6] Z. Zhao, A. Kunar, R. Birke, and L. Y. Chen, “CTAB-GAN: Effective Table Data Synthesizing,” in Asian Conference on Machine Learning. PMLR, 2021, pp. 97–112.  
[7] Z. Zhao, A. Kunar, R. Birke, H. Van der Scheer, and L. Y. Chen, “CTAB-GAN+: Enhancing Tabular Data Synthesis,” Frontiers in big Data, vol. 6, p. 1296508, 2024.   

**Time** ： 27/11/2024  
**Author** ： Chuang Liu   
**Email** ：LIUC0316@126.COM     
