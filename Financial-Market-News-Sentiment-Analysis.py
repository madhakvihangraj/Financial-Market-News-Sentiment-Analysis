# -*- coding: utf-8 -*-
"""Project-2n.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mPfMwZfBm-2AvD-oNufKGIXC7Q5cll5U

# **Financial Market News - Sentiment Analysis**

This is a data (dummy) of Financial Market Top 25 News for the Day and Task is to Train and Predict Model for Overall Sentiment Analysis

# **Import Library**
"""

import pandas as pd

import numpy as np

"""# **Import Dataset**"""

df = pd.read_csv(r'https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Financial%20Market%20News.csv', encoding = "ISO-8859-1")

df.head()

df.info()

df.shape

df.columns

"""# **Get Feature Selection**"""

' '.join(str(x) for x in df.iloc[1,2:27])

df.index

len(df.index)

news = []
for row in range(0,len(df.index)):
  news.append(' '.join(str(x) for x in df.iloc[1,2:27]))

type(news)

news[0]

X = news

type(X)

"""# **Get Feature Text Conversoin to Bag of Words**"""

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(lowercase = True, ngram_range=(1,1))

X = cv.fit_transform(X)

X.shape

y = df['Label']

y.shape

"""# **Get Train Test Split**"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify = y, random_state = 2529)

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=200)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

confusion_matrix(y_test, y_pred)

print(classification_report(y_test, y_pred))