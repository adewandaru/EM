# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 06:40:02 2018
EM algorithm toy example: 1 Dimensional.

@author: dewandaru@gmail.com

inspired by Victor Lavrenko's explanation on solving Mixture model using EM.

"""



import matplotlib.pyplot as plt
import numpy as np
import math


# This is the the training data. enter the two Gaussian distribution's mu and sigma as you wish.
# we start with [3, 7] and generate the graphics from that distribution.
mu1 = 3
sigma1 = 1
mu2 = 7
sigma2 = 1

num = 1000

t1 = np.random.normal(mu1, sigma1, num)
plt.figure(0)
plt.hist(t1, bins= num/10, color='r')


t2 = np.random.normal(mu2, sigma2, num)
plt.hist(t2, bins= num / 10, color ='b')

x = np.concatenate([t1,t2])
np.random.shuffle(x)

'''
 EM algorithm is iterative between calculating :
 1. Expectation membership p(cluster|x) and
 then 
 2. Finding parameter which Maximizing the *likelihood* / 
 [moving cluster center's mu and sigma]
'''

mu = [0, 1]
sigma = [1, 1]



def prior(pcx):
    return pcx.mean()

def p_x_given_c(x, mu, sigma_squared):
    ''' just a typical normal pdf '''
    return np.exp( -(x-mu)**2 / (2 * sigma_squared) ) / np.sqrt( 2 * math.pi * sigma_squared )   

def p_c_given_x(x, mu1, sigma1, mu2, sigma2, prior):
    ''' 
    calculate responsibility p(c|x) for each datapoint. where c is the cluster.
                   p(x|c) p(c)              p(x|c) p(c)                  p(x|c) p(c) [prior]
    p(c|x) =  --------------------- = ------------------------- =  -------------------------------
                      p(x)                  sum(c) p(x,c)             p(x|c) p(c) + p(x|c') p(c')  
    '''
    nom = p_x_given_c(x, mu1, sigma1) * prior
    evidence = nom + p_x_given_c(x, mu2, sigma2 ) * (1-prior)
    return nom / evidence

pcfx = np.vectorize(p_c_given_x)

pa = 0.5
pb = 0.5

for i in range(100):
    print "#"+str(i)
    '''
    Expectation step: calculate "responsibility" of each cluster to each datapoints.
    i.e which 
    p_c1 = P(c1|x) = ...
    p_c2 = P(c2|x) = ...
    '''
    
    a = p_c_given_x( x, mu[0], sigma[0], mu[1], sigma[1], pa )
    b = 1 - a
    
    
    pa = prior(a)
    pb = 1 - pa
    
    '''
    Maximization of Likelihood 
    adjust mu and sigma 
    '''
    mu[0] = np.multiply(a, x).sum() / a.sum()
    sigma[0] = np.multiply(a, (x - mu[0])**2).sum() / a.sum() 
    
    mu[1] = np.multiply(b, x).sum() / b.sum()
    sigma[1] = np.multiply(b, (x - mu[1])**2).sum() / b.sum() 
    
    print "mu"
    print mu
    print "sigma" 
    print sigma
    
    ''' this part is for visualization only '''
    _t1 = x[np.where( a > 0.5 )]
    _t2 = x[np.where( a <= 0.5 )]
    
    plt.figure(i+1)
    
    if (len(_t1)>0):
        # max - min / width = bins
        b = int((_t1.max() - _t1.min()) / 0.05)
        plt.hist(_t1, bins=b, color='r')
        plt.axvline(x=mu[0], color='r', linestyle="--")
    if (len(_t2)>0):
        b = int((_t2.max() - _t2.min()) / 0.05)
        plt.hist(_t2, bins=b, color='b')
        plt.axvline(x=mu[1], color="b", linestyle="--")
        
    y = [30] * len(x)
    
    plt.scatter(x,y,c=a, cmap=plt.cm.get_cmap('RdBu_r'), zorder = 100)
    plt.savefig("img"+str(i)+".png")

    


    


     
    
