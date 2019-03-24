# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:26:19 2019

# @author: Sandi Šegota
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)

plt.figure()
plt.plot(x,y, label = "f(x)=$sin(x)$")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

np.random.seed(0)
n = 1000
x = np.random.uniform(-10,10,size=n)
y = np.sin(x)

plt.figure()
plt.scatter(x,y, label = "f(x)=$sin(x)$")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

X = np.reshape(x, [n,1])
y = np.reshape(y, [n, ])

clf1 = MLPRegressor(alpha = 0.001,\
                    hidden_layer_sizes = (10, ),\
                    max_iter = 800,\
                    activation = "logistic",\
                    verbose = True,\
                    learning_rate = "adaptive",\
                    solver = "lbfgs")

clf1.fit(X,y)

x_ = np.linspace(-10,10,1600)
pred_x = np.reshape(x_, [1600,1])
pred_y = clf1.predict(pred_x)

plt.figure()
plt.plot(x_, np.sin(x_), color = "b", label = "$f_{original}$(x)=s$in(x)$")
plt.plot(pred_x, pred_y, color = "r", label= "$f_{MLP}$(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

print("clf1.loss_= "+str(clf1.loss_))
print("clf1.n_iter_= ", str(clf1.n_iter_))
print("clf1.coefs_= " + str(clf1.coefs_))
print("clf1.intercepts_ = " + str(clf1.intercepts_))