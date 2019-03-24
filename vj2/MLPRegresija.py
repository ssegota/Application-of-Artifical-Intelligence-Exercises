# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:08:11 2019

@author: Sandi Šegota
"""

#Multi layer Perceptron MLP

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

x = np.arange(-10,10,0.1)
y = x**2

plt.figure()
plt.plot(x,y, label = "f(x)=$x^2$")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

np.random.seed(0)
n = 100
x = np.random.uniform(-15,15,size=n)
y = x**2

plt.figure()
plt.scatter(x,y, label = "f(x)=$x^2$")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

X = np.reshape(x, [n,1])
y = np.reshape(y, [n, ])

clf1 = MLPRegressor(alpha = 0.01,
                   hidden_layer_sizes = (100,),\
                   max_iter=20000, \
                   activation = "logistic",\
                   verbose = True,\
                   learning_rate = "adaptive",\
                   tol = 0.000001)

a = clf1.fit(X, y)

#Podaci za testiranje
x_ = np.linspace(-10,10,1600)
pred_x = np.reshape(x_, [1600, 1])
pred_y = clf1.predict(pred_x)

plt.figure()
plt.plot(x_,x_**2, color = "b", label = "$f_{original}$(x)=$x^2$")
plt.plot(pred_x, pred_y, color="r", label="$f_{MLP}$=(x)")
plt.grid(True)
plt.title("Comparison between real data and predicted data")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

clf1.coefs_  #Težinske vrijednosti
clf1.intercepts_ #Biasi
clf1.n_iter_ #Broj iteracija
clf1.n_outputs_ #Broj outputa