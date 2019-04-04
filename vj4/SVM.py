# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:04:05 2019

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
###
#Ulazni podaci
###
x = [1,2,3,4,9,12,14,17,20]
y = [2,8,3,9,5,10,6,13,4]

plt.figure()
plt.scatter(x,y)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

X = np.array([[1,2],
              [2,8],
              [3,3],
              [4,9],
              [9,5],
              [12,10],
              [14,6],
              [17,13],
              [20,4]])

y = [0,1,0,1,0,1,0,1,0]

###
#definiranje SVM
###
#SVC = support vector classifier
clf = svm.SVC(kernel = "linear", C = 1.0)
clf.fit(X,y)
print("test_prediction 1 = " + str(clf.predict([[0.4, 0.3]])))
print("test_prediction 2 = " + str(clf.predict([[14, 12]])))
###
#Konstrukcije hiperravnine
###
w = clf.coef_[0]
print("w = " + str(w))
#a - nagib hiperravnine
a = -w[0]/w[1]
print("a = " + str(a))

xx = np.linspace(0,22)
yy = a*xx - clf.intercept_[0]/w[1]

###
#graficki prikaz hiperravnine
###
plt.figure()
plt.plot(xx,yy)
plt.scatter(X[:,0],X[:,1])
plt.xlim(0,22)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()