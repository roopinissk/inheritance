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


#data analysis
disorder_count = gen_clean['Genetic Disorder'].value_counts()

#plot
disorder_count.plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
plt.show()

# plot subclass of disorders
subclass_count = gen_clean['Disorder Subclass'].value_counts()
plt.figure(figsize=(10, 6))
subclass_count.plot(kind= 'bar', width= 0.5, color= 'skyblue')
plt.title('Disorder Subclass Count')
plt.xlabel('Disorder Subclass')
plt.xticks(rotation=45)
plt.ylabel('Count')
plt.show()

#########################################

# Probability 

#probability of a disorder given the maternal gene influence
probability_maternal = gen_clean.groupby('Maternal gene')['Disorder Subclass'].value_counts(normalize=True).unstack()
print(probability_maternal)


#probability of a disorder given paternal gene influence
probability_paternal = gen_clean.groupby('Paternal gene')['Disorder Subclass'].value_counts(normalize=True).unstack()
print(probability_paternal)


#plots
probability_maternal.plot(kind='bar', stacked=True, figsize=(10, 6), cmap='tab20')
plt.title('Probability by maternal gene status')
plt.xlabel('Maternal gene')
plt.ylabel('Probability')
plt.legend(title='Disorder Subclass', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

probability_paternal.plot(kind='bar', stacked=True, figsize=(10, 6), cmap='tab20')
plt.title('Probability by paternal gene status')
plt.xlabel('Paternal gene')
plt.ylabel('Probability')
plt.legend(title='Disorder Subclass', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
