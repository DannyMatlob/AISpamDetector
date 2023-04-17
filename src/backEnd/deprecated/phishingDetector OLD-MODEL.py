# importing required libraries
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler
import modelTrainers
import os

# find source file for training
phishingDataSrc = "../../trainingData/phishing/phishing.csv"
abs_path = os.path.abspath(phishingDataSrc)

# reading csv file and extracting class column to y.
data = pd.read_csv(abs_path)

# extracting F important features from x
f = 12
columnList = load("columns.joblib")
columnList = columnList[:f]
print(columnList)
y = data['phishing']
x = data[columnList]

#Only train on the first N rows
n = 30000
testN = 20000

trainingX = x[:n]   
trainingY = y[:n]
testingX = x[-testN:].reset_index(drop=True)
testingY = y[-testN:].reset_index(drop=True)

#Scale the data
scaling = MinMaxScaler(feature_range=(-1,1)).fit(trainingX)
trainingX = scaling.fit_transform(trainingX)
testingX = scaling.fit_transform(testingX)

print("Training ", n, "rows on top", f, " features")

modelTrainers.SVM(trainingX, trainingY, testingX, testingY)
#modelTrainers.RFC(trainingX, trainingY, testingX, testingY)



