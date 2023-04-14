import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

pd.set_option('display.max_columns', None)
plt.rcParams['figure.figsize'] = (12,6)


phishingDataSrc = "../../trainingData/phishing/phishing.csv"
abs_path = os.path.abspath(phishingDataSrc)

# Reading csv file and extracting class column to y.
data = pd.read_csv(abs_path)
data.rename(columns={'phishing': 'labels'}, inplace=True)

# Convert data to 32 bit numbers to save memory
float_cols = data.select_dtypes('float64').columns
for c in float_cols:
    data[c] = data[c].astype('float32')
    
int_cols = data.select_dtypes('int64').columns
for c in int_cols:
    data[c] = data[c].astype('int32')
    

def corr_heatmap(data, idx_s, idx_e):
    y = data['labels']
    temp = data.iloc[:, idx_s:idx_e]
    if 'id' in temp.columns:
        del temp['id']
    temp['labels'] = y
    sns.heatmap(temp.corr(), annot=True, fmt='.2f')
    plt.show()

corr_heatmap(data, 10, 112)