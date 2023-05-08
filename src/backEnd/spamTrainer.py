import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
import os
import pickle

abs_path_email_body_dataset = os.path.abspath('../../trainingData/completeSpamAssassin2.csv')
print(abs_path_email_body_dataset)

df_body = pd.read_csv('E:\Projects\Python\CS166\phishingDetector\AISpamDetector\\trainingData\spam\completeSpamAssassin2.csv') #dataset for training body of email. 1 - spam 0 - ham
df_subject = pd.read_csv('E:\Projects\Python\CS166\phishingDetector\AISpamDetector\\trainingData\spam\spam_ham_dataset.csv')#dataset for training subject of email. 1 - spam 0 - ham
df_test = pd.read_csv('E:\Projects\Python\CS166\phishingDetector\AISpamDetector\\trainingData\spam\\fraud_email_.csv')#dataset for testing. 1 - spam, 0 - ham
# print(df_body.head())
# print(df_body.tail())
# print(df_body.shape)
# print("df_body size: ",df_body.size)
# print(df_body.count())
# print(df_body['Label'].value_counts())

# print("df_body_train size: ",df_body.size)
# print("df_subject_train size: ",df_subject.size)

#drop any rows with null data
df_body = df_body.dropna(subset=['Body'])   
df_subject = df_subject.dropna(subset=('text')) 
df_test = df_test.dropna(subset=('Text'))
print("df_body_train size: ",df_body.size)
# print("df_subject_train size: ",df_subject.size)

x_body = df_body["Body"]
y_body = df_body["Label"]
x_subject = df_subject["text"]
y_subject = df_subject["label_num"]
x_test = df_test['Text']
y_test = df_test['Class'] # expected dependent value of y for test data

#Vectorizer to determine the TF-IDF (term frequency) of the raw data
vectorizer_body = TfidfVectorizer()
vectorizer_subject = TfidfVectorizer()

#learn the vocav and the idf > document term matrix
x_body_features = vectorizer_body.fit_transform(x_body)
# x_subject_features = vectorizer_subject.fit_transform(x_subject)

print("x_body_features shape: ",x_body_features.shape)

#model to use
model_body = LogisticRegression()
# model_subject = LogisticRegression()

#train data
model_body.fit(x_body_features,y_body)
# model_subject.fit(x_subject_features,y_subject)

#save trained model
with open('trained_spam_email_dataset_model','wb') as f:
    pickle.dump(model_body,f)
    
with open('trained_spam_email_dataset_model','rb') as f:
    trained_model = pickle.load(f)
    

#test model using a 3rd dataset
input_mail_feature = vectorizer_body.transform(x_test)
prediction = trained_model.predict(input_mail_feature)

#check accuracy
accuracy_score_on_testData = accuracy_score(prediction,y_test)

print('Accuracy: ', accuracy_score_on_testData)
