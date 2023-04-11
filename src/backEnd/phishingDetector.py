
# importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

phishingDataSrc = "../../trainingData/phishing/phishing.csv"
abs_path = os.path.abspath(phishingDataSrc)

# reading csv file and extracting class column to y.
x = pd.read_csv(abs_path)
a = np.array(x)
y = a[:,49] # classes having 0 and 1

# extracting two features
x = np.column_stack((x.NumDots,x.UrlLength))

# 569 samples and 2 features
x.shape

print (x),(y)
