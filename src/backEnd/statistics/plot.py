# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import time
import os

# find source file for training
phishingDataSrc = "../../trainingData/phishing/phishing.csv"
abs_path = os.path.abspath(phishingDataSrc)

# reading csv file and extracting class column to y.
data = pd.read_csv(abs_path)

# extracting F important features from x
f = 5
columnList = load("columns.joblib")
columnList = columnList[:f]
print(columnList)
y = data['phishing']
x = data[columnList]

#Only train on the first N rows
n = 1000

trainingX = x[:n]
trainingY = y[:n]

#Scale the data
scaling = MinMaxScaler(feature_range=(-1,1)).fit(trainingX)
scaledX = scaling.fit_transform(trainingX)

fig, ax = plt.subplots(1, 2, figsize=(15, 3))
sns.histplot(trainingX, ax=ax[0], kde=True, legend=False)
ax[0].set_title("Original Data")
sns.histplot(scaledX, ax=ax[1], kde=True, legend=False)
ax[1].set_title("Scaled data")
plt.show()