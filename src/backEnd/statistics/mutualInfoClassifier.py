import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', None)  # Display all columns in a single line

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
    

#
# Mutual Info Classifier 
#
from sklearn.feature_selection import mutual_info_classif
X = data.drop(['labels'], axis=1)
y = data['labels']
discrete_features = X.dtypes == int

mi_scores = mutual_info_classif(X, y, discrete_features=discrete_features)
mi_scores = pd.Series(mi_scores, name='MI Scores', index=X.columns)
mi_scores = mi_scores.sort_values(ascending=False).index.tolist()

#Write output to a text file
print("Writing to txt file")
with open('mi_scores.txt', 'w') as f:
    from joblib import dump, load
    dump(mi_scores, 'columns.joblib') 
    np.set_printoptions(threshold=np.inf)
    print(mi_scores, file=f)
print("Write finished")