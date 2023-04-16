import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression


df_body = pd.read_csv('trainingData\completeSpamAssassin2.csv')
df_subject = pd.read_csv('trainingData\spam_ham_dataset.csv')
print(df_body.head())
print(df_body.tail())
print(df_body.shape)
print("df_body size: ",df_body.size)
print(df_body.count())
print(df_body['Label'].value_counts())

print("df_body_train size: ",df_body.size)
print("df_subject_train size: ",df_subject.size)
df_body = df_body.dropna(subset=['Body'])   
df_subject = df_subject.dropna(subset=('text')) 
print("df_body_train size: ",df_body.size)
print("df_subject_train size: ",df_subject.size)

x_body = df_body["Body"]
y_body = df_body["Label"]
x_subject = df_subject["text"]
y_subject = df_subject["label_num"]

#Vectorizer to determine the TF-IDF (term frequency) of the raw data
vectorizer = TfidfVectorizer()

#learn the vocav and the idf > document term matrix
x_body_features = vectorizer.fit_transform(x_body)
x_subject_features = vectorizer.fit_transform(x_subject)

print("x_body_features shape: ",x_body_features.shape)

model_body = LogisticRegression()
model_subject = LogisticRegression()
model_body.fit(x_body_features,y_body)
model_subject.fit(x_subject_features,y_subject)

# input_mail_feature = vectorizer.transform(df_subject['text'])
# prediction = model.predict(input_mail_feature)
# print(prediction[0])
