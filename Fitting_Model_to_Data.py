
# coding: utf-8

# In[46]:


import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import optimize
import os
import random


# In[57]:


# Exercise 1

ID = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = [203, 58, 210, 202, 198, 158, 165, 201, 157, 131, 166, 160, 186, 125, 218, 146]
y = [495, 173, 479, 504, 510, 416, 393, 442, 317, 311, 400, 337, 423, 334, 533, 344]
sigma_y = [21, 15, 27, 14, 30, 16, 14, 25, 52, 16, 34, 31, 42, 26, 16, 22]
sigma_x = [5, 9, 4, 4, 11, 7, 5, 5, 5, 6, 6, 5, 9, 8, 6, 5]
rho_xy = [-0.33, 0.67, -0.02, -0.05, -0.84, -0.69, 0.30, -0.46, -0.03, 0.50, 0.73, -0.52, 0.90, 0.40, -0.78, -0.56]

# initializing matrices
A = np.zeros((len(ID), 2))
C = np.zeros((len(ID), len(ID)))
Y = np.zeros(len(ID),)

# filling matrices
for i in range(len(ID)):
    Y[i] = y[i]
    A[i][0] = 1
    A[i][1] = x[i]
    C[i][i] = sigma_y[i]
    

# Defining the Chi square function.
def chi_sq(z):
    m = z[0];
    b = z[1]
    X2 = 0;
    for i in range(len(y)):
        X2 = X2 + ((y[i] - m*x[i] - b)**2)/(sigma_y[i]**2)
    return X2

# Plotting data
plt.errorbar(x,y,sigma_y, color = 'k', fmt = 'o')

# Minimizing the chi-squared function, and using the best fit parameters to define points for a best fit line.
result = optimize.minimize(chi_sq, [20, 150])
x_best = np.linspace(min(x),max(x))
y_best = result.x[0]*x_best + result.x[1]

# Plotting best fit line
plt.plot(x_best,y_best, 'k-')


# In[48]:


print(result.x[0])
print(result.x[1])


# In[59]:


# Exercise 2

# Adding additional entries to data
ID.extend([1, 2, 3, 4])
x.extend([201, 244, 47, 287])
y.extend([592, 401, 583, 402])
sigma_y.extend([61, 25, 38, 15])
sigma_x.extend([9, 4, 11, 7])
rho_xy.extend([-0.84, 0.31, 0.64, -0.27])

# Plotting data
plt.errorbar(x,y,sigma_y, color = 'k', fmt = 'o')

# Minimizing the chi-squared function, and using the best fit parameters to define points for a best fit line.
result = optimize.minimize(chi_sq, [20, 150])
x_best = np.linspace(min(x),max(x))
y_best = result.x[0]*x_best + result.x[1]

slope = result.x[0]
y_int = result.x[1]

# Plotting best fit line
plt.plot(x_best,y_best, 'k-')


# In[50]:


result.x[1]


# In[51]:


# Exercise 3

# Redefining data without the outliers
ID = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = [203, 58, 210, 202, 198, 158, 165, 201, 157, 131, 166, 160, 186, 125, 218, 146]
y = [495, 173, 479, 504, 510, 416, 393, 442, 317, 311, 400, 337, 423, 334, 533, 344]
sigma_y = [21, 15, 27, 14, 30, 16, 14, 25, 52, 16, 34, 31, 42, 26, 16, 22]
sigma_x = [5, 9, 4, 4, 11, 7, 5, 5, 5, 6, 6, 5, 9, 8, 6, 5]
rho_xy = [-0.33, 0.67, -0.02, -0.05, -0.84, -0.69, 0.30, -0.46, -0.03, 0.50, 0.73, -0.52, 0.90, 0.40, -0.78, -0.56]

# Defining the Chi square function.
def chi_sq(z):
    q = z[0];
    m = z[1];
    b = z[2];
    X2 = 0;
    for i in range(len(y)):
        X2 = X2 + ((y[i] - q*x[i]**2 - m*x[i] - b)**2)/(sigma_y[i]**2)
    return X2

# Plotting data
plt.errorbar(x,y,sigma_y, color = 'k', fmt = 'o')

# Minimizing the chi-squared function, and using the best fit parameters to define points for a best fit line.
result = optimize.minimize(chi_sq, [1, 20, 150])
x_best = np.linspace(0,300)
y_best = result.x[0]*x_best**2 + result.x[1]*x_best + result.x[2]

# Plotting best fit line
plt.plot(x_best,y_best, 'k-')
plt.xlim(0,300)
plt.ylim(0,700)


# # Exercise 4
# 
# ![exercise_4.jpg](attachment:exercise_4.jpg)

# In[52]:


# Exercise 5

# This exericise asked us to look at the matrix formulation for the Chi^2 forumula which I don't think will be relevant for
# starting the research, so I'm going to skip this exercise at least for now.


# In[53]:


# Exercise 6

# 
ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = [201, 244, 47, 287, 203, 58, 210, 202, 198, 158, 165, 201, 157, 131, 166, 160, 186, 125, 218, 146]
y = [592, 401, 583, 402, 495, 173, 479, 504, 510, 416, 393, 442, 317, 311, 400, 337, 423, 334, 533, 344]
sigma_y = [61, 25, 38, 15, 21, 15, 27, 14, 30, 16, 14, 25, 52, 16, 34, 31, 42, 26, 16, 22]
sigma_x = [9, 4, 11, 7, 5, 9, 4, 4, 11, 7, 5, 5, 5, 6, 6, 5, 9, 8, 6, 5]
rho_xy = [-0.84, 0.31, 0.64, -0.27-0.33, 0.67, -0.02, -0.05, -0.84, -0.69, 0.30, -0.46, -0.03, 0.50, 0.73, -0.52, 0.90, 0.40, -0.78, -0.56]

# Writing out the likelihood (eventually posterior)
def Likelihood(m,b,P_b, Y_b, V_b):
    L = 0;
    for i in range(len(ID)):
        L = L + np.log(((1 - P_b)/np.sqrt(2*np.pi*sigma_y[i]**2))*np.exp(-((y[i] - m*x[i] - b)**2)/(2*sigma_y[i]**2)) +     P_b/(np.sqrt(2*np.pi*(sigma_y[i]**2 + V_b)))*np.exp(-((y[i] - Y_b)**2)/(2*(sigma_y[i]**2 + V_b))))
    return L

# MCMC
data = np.zeros((1000,2))
data[0][0] = 15
data[0][1] = 150
for i in range(1000):
    L = Likelihood(15,150,0.2,0,20)


# In[61]:


def MCMC(m,b,P_b, V_b, Y_b, n = 100): # n is the number of iterations run
    L = Likelihood(m,b,P_b, V_b, Y_b)
    params = np.zeros((5,n))
    for i in range(n): 
        # Moving to a new spot in parameter space
        m_new = m + np.random.normal(0,1)
        b_new = b + np.random.normal(0,1)
        P_b_new = P_b + np.random.normal(0,1)
        V_b_new = V_b + np.random.normal(0,1)
        Y_b_new = Y_b + np.random.normal(0,1)
        
        # finding new likelihood at this spot
        L_new = Likelihood(m_new,b_new,P_b_new, V_b_new, Y_b_new)
        
        # finding difference between old and new values
        d = L_new - L
        u = random.uniform(0,1) # defining the random number to be accepted or rejected
        if d >= np.log(u):
            L = L_new
            m = m_new
            b = b_new
            P_b = P_b_new
            V_b = V_b_new
            Y_b = Y_b_new
            params[0][i] = m
            params[1][i] = b
            params[2][i] = P_b
            params[3][i] = V_b
            params[4][i] = Y_b
        else:
            params[0][i] = m
            params[1][i] = b
            params[2][i] = P_b
            params[3][i] = V_b
            params[4][i] = Y_b
     # Creating subplots
    f, ax = plt.subplots(1, 3, figsize=[17,5])
    f.subplots_adjust(wspace=0.3)
    
    ax[0].plot(params[1], params[0],'k.')
    ax[0].set_xlabel('b')
    ax[0].set_ylabel('m')
    
    ax[1].hist(params[0], bins = 50)
    ax[1].set_xlabel('m')
    ax[1].set_ylabel('frequency')
    
    ax[2].hist(params[1], bins = 10)
    ax[2].set_xlabel('b')
    ax[2].set_ylabel('frequency')
    
    plt.savefig('MCMC.png')
    
    return L, params


# In[62]:


L, params = MCMC(0.5, 200, 0.1, 1, 1, n = 10000)


# In[60]:


# The actual slope 
print('The actual slope is ' + str(slope))
print('The actual y-intercept is ' + str(y_int))

