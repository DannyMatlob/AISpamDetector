# importing required libraries
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler
import modelTrainers
import os

# find source file for training
phishingDataSrc = "../../trainingData/phishing/PhishingBETTER.csv"
abs_path = os.path.abspath(phishingDataSrc)

# reading csv file and extracting class column to y.
data = pd.read_csv(abs_path)

# extracting features from x
y = data['phishing']
x = data.iloc[:, :10]

'''
print(x,"\n")
print(y)
#exit()
'''

#Only train on the first N rows
n = 10000
testN = 5000

trainingX = x[:n]   
trainingY = y[:n]
testingX = x[-testN:].reset_index(drop=True)
testingY = y[-testN:].reset_index(drop=True)

#Scale the data
scaling = MinMaxScaler(feature_range=(-1,1)).fit(trainingX)
trainingX = scaling.fit_transform(trainingX)
testingX = scaling.fit_transform(testingX)

print("Training ", n, "rows")

#modelTrainers.SVM(trainingX, trainingY, testingX, testingY)
modelTrainers.RFC(trainingX, trainingY, testingX, testingY)



