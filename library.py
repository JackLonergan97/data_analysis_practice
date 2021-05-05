# Library of functions for data_analysis_practice
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import optimize
import os
import random
import argparse

ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = [201, 244, 47, 287, 203, 58, 210, 202, 198, 158, 165, 201, 157, 131, 166, 160, 186, 125, 218, 146]
y = [592, 401, 583, 402, 495, 173, 479, 504, 510, 416, 393, 442, 317, 311, 400, 337, 423, 334, 533, 344]
sigma_y = [61, 25, 38, 15, 21, 15, 27, 14, 30, 16, 14, 25, 52, 16, 34, 31, 42, 26, 16, 22]
sigma_x = [9, 4, 11, 7, 5, 9, 4, 4, 11, 7, 5, 5, 5, 6, 6, 5, 9, 8, 6, 5]
rho_xy = [-0.84, 0.31, 0.64, -0.27-0.33, 0.67, -0.02, -0.05, -0.84, -0.69, 0.30, -0.46, -0.03, 0.50, 0.73, -0.52, 0.90, 0.40, -0.78, -0.56]

# Finding the likelihood from a data set
def Likelihood(m,b,P_b, Y_b, V_b, data): # data is the array [ID, x, y, sigma_x, sigma_y, rho_xy]
    L = 0;
    for i in range(len(data[0])):
        L = L + np.log(((1 - P_b)/np.sqrt(2*np.pi*data[0][i]**2))*np.exp(-((data[2][i] - m*data[1][i] - b)**2)/(2*data[4][i]**2)) + P_b/(np.sqrt(2*np.pi*(data[4][i]**2 + V_b)))*np.exp(-((data[2][i] - Y_b)**2)/(2*(data[4][i]**2 + V_b))))
    return L

# Running the Metropolis-Hasting MCMC algorithm
def MCMC(m,b,P_b, V_b, Y_b, data, n = 10000): # n is the number of iterations run
#     n = args.runs
    print('running MCMC with n = ' + str(n))
    L = Likelihood(m,b,P_b, V_b, Y_b, data)
    params = np.zeros((n,5))
    for i in range(n): 
        # Moving to a new spot in parameter space
        m_new = m + np.random.normal(0,1)
        b_new = b + np.random.normal(0,1)
        P_b_new = P_b + np.random.normal(0,1)
        V_b_new = V_b + np.random.normal(0,1)
        Y_b_new = Y_b + np.random.normal(0,1)
        
        # finding new likelihood at this spot
        L_new = Likelihood(m_new,b_new,P_b_new, V_b_new, Y_b_new, data)
        
        # finding difference between old and new values
        d = L_new - L
        u = random.uniform(0,1)
        if d >= np.log(u):
            L = L_new
            m = m_new
            b = b_new
            P_b = P_b_new
            V_b = V_b_new
            Y_b = Y_b_new
            params[i][0] = m
            params[i][1] = b
            params[i][2] = P_b
            params[i][3] = V_b
            params[i][4] = Y_b
        else:
            params[i][0] = m
            params[i][1] = b
            params[i][2] = P_b
            params[i][3] = V_b
            params[i][4] = Y_b
    return L, params

# Creating subplots
def Figures(params): 
    f, ax = plt.subplots(1, 3, figsize=[17,5])
    f.subplots_adjust(wspace=0.3)
    
    ax[0].plot(params[:,1], params[:,0],'k.')
    ax[0].set_xlabel('b')
    ax[0].set_ylabel('m')
    
    ax[1].hist(params[:,0], bins = 50)
    ax[1].set_xlabel('m')
    ax[1].set_ylabel('frequency')
    
    ax[2].hist(params[1:,], bins = 10)
    plt.savefig('MCMC.png')
    return
