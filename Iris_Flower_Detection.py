# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:56:13 2020

@author: suhail
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
dataset=load_iris()

X=dataset.data
y=dataset.target

#Visualizing the data
plt.plot(X[:,0][y==0],X[:,1][y==0],'r.',label='Setosa')#category 1
plt.plot(X[:,0][y==1],X[:,1][y==1],'g.',label='Versicolor')#category 2
plt.plot(X[:,0][y==2],X[:,1][y==2],'b.',label='Virginica')#category 3
plt.legend()
plt.show()

#Standardizing the data
from sklearn.preprocessing import StandardScaler
X=StandardScaler().fit_transform(X)

#splitting the data into training and test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

# Training the Logistic Regression model on the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

accuracy=classifier.score(X_test,y_test)
print(accuracy)