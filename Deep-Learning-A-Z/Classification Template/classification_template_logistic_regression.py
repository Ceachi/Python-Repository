# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:07:29 2020

@author: Ceachi
"""

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_age_purched(X,y):      
    Z1 =  [row[0] for row in X]
    
    df = pd.DataFrame({
        'age':   Z1,
        'purched':   y
    })    
    # a scatter plot comparing num_children and num_pets
    df.plot(kind='scatter',x='age',y='purched',color='red')
    plt.show()


#Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

plot_age_purched(X,y) #asta e doar ca sa vizualizez un plot intre [age,purched]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split #model_selection = cross_validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
