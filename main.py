import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# data preprocessing

gen = pd.read_csv('/Users/rubee/Documents/nyu_fall/methods_2024/inheritance/genetic_disorders.csv')
gen.head()

#drop na
na_count = gen.isna().sum()

gen_clean = gen.dropna()
print(gen_clean.shape)

#before cleaning shape (22083, 45)
#after cleaning shape (5307, 45)

# print(gen_clean.columns)

#has PII and irrelevant data 

gen_clean = gen_clean.drop(columns = ['Patient Id', 'Patient First Name', 'Family Name', "Father's name", 'Institute Name', 'Location of Institute', 'Test 1', 'Test 2', 'Test 3', 'Test 4',
       'Test 5', 'Parental consent', 'Place of birth', 'Blood test result',
       'Symptom 1', 'Symptom 2', 'Symptom 3', 'Symptom 4', 'Symptom 5' ])

#verifying column names and NAs
print(gen_clean.columns)
print(gen_clean.isna().sum())  #all clean

