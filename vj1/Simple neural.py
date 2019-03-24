# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 19:19:45 2019

@author: Sandi Šegota
"""

import numpy as np
import matplotlib.pyplot as plt

def Sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-5,5,0.1)
y = []

for i in range(len(x)):
    y.append(Sigmoid(x[i]))

plt.figure()
plt.plot(x,y)
plt.title("Example of Sigmoid function")
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.legend()
plt.grid(True)
plt.show()
X = np.array([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
#željene izlazne
y = np.array([[0,0,1,1]]).T
np.random.seed(0)

#inicijalizirati težinske faktore
syn0 = 2 * np.random.random((3,1))-1
print("syn0 = " + str(syn0))

noIterations = np.arange(0,10000,1)

OutList1 = list()
OutList2 = list()
OutList3 = list()
OutList4 = list()
syn0_1 = list()

for i in range(len(noIterations)):
    #Ulazni layer
    l0 = X
    #slijedeći layer
    l1 = Sigmoid(np.dot(l0,syn0))
    #update vrijednosti atributa
    OutList1.append(l1[0])
    OutList2.append(l1[1])
    OutList3.append(l1[2])
    OutList4.append(l1[3])
    #izračun pogreške
    l1_error = y - l1
    #print("l1_error", l1_error)
    #aktivacija
    l1_delta = l1_error * Sigmoid(l1)
    #update težinskih faktora
    syn0 += np.dot(l0.T, l1_delta)

print("l1 = " + str(l1))
print("syn0 = " + str(syn0))

plt.figure()
plt.plot(noIterations, OutList1, label="OutValue1")
plt.plot(noIterations, OutList2, label="OutValue2")
plt.plot(noIterations, OutList3, label="OutValue3")
plt.plot(noIterations, OutList4, label="OutValue4")
plt.xlabel("Number of Iterations")
plt.xlim(0,200)
plt.ylabel("OutValue")
plt.grid(True)
plt.legend()
plt.show()
