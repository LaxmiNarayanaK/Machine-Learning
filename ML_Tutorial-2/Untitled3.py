#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3]
t = [1.2,1.9,3.2]


# In[3]:


def parameters(x,y):
 A = np.sum(x)
 B = np.sum(y)
 C = np.dot(x,x)
 D = np.dot(x,y)
 N = len(x)
 
 w1 = (B*A-D*N)/(A**2 - C*N)
 w0 = (D - w1*C)/A
 return (w1,w0)


# In[5]:


slope,intercept = parameters(x,t)
y_eqt = []
for i in range(len(x)):
    y_eqt.append(slope*x[i] + intercept)
plt.scatter(x,t,)
plt.plot(x,y_eqt,"g-")


# In[ ]:




