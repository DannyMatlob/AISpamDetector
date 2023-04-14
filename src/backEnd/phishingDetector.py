
# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

phishingDataSrc = "../../trainingData/phishing/phishing.csv"
abs_path = os.path.abspath(phishingDataSrc)

# reading csv file and extracting class column to y.
x = pd.read_csv(abs_path)

#Convert CSV to arrays
a = np.array(x)
y = a[:,111] # Column 112 | 1: Phishing, Non-Phishing: 0

# extracting two features from X
x = np.column_stack((x.qty_redirects, x.tls_ssl_certificate))

#Only train on the first 10000 rows
trainingX = x[:10000]
trainingY = y[:10000]
testingX = x[-10000:]
testingY = y[-10000:]

# 58645 Samples
x.shape

print ("Length of x:", len(trainingX))
print(x)
print ("Length of y:", len(trainingY))
print(y)

print("Training")
# import support vector classifier 
# "Support Vector Classifier"
from sklearn.svm import SVC  
clf = SVC(kernel='linear') 
  
# fitting x samples and y classes 
clf.fit(x, y) 

#Save the model to a file
print("Saving the Model")
from joblib import dump, load
dump(clf, 'testModel.joblib') 

#Run tests
print("Predicting")
print("0 0",clf.predict([[0, 0]]))
print("1 0",clf.predict([[1, 0]]))
print("0 1",clf.predict([[0, 1]]))
print("0 2",clf.predict([[0, 2]]))



