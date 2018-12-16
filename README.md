# EM Algorithm 1d Example.
EM algorithm samples in Gaussian Mixture Model
This code inspired by Victor Lavrenko's explanation https://www.youtube.com/watch?v=REypj2sy_5U&t=170s
on solving Mixture model using EM.

#1 Dimensional EM
Check the em-algorithm-1d.py on this repository.

The program create two sets of 1000 gaussian random 1 dimensional datapoints 
(scalar) each with specific mean and variance.

Then it merges and shuffle the points (totaling 2000 points), we want to know if
the EM algorithm derived from GMM is able to find the clusters (including mean and variance) 
of each 2000 datapoints.

the EM algorithm derived here is done in a limited number of iterations (100)
and is alternating between estimation of expectation membership and finding centroid
of each clusters. This is very similar to K-means, but the EM is having soft 
clustering, meaning that each datapoint is having membership weight, and not a hard
assignment of membership like in K-means clustering.

Note the limitation:
    - only two clusters (K=2)
    - focused for pedagogical purpose instead of performance.

The simulation works best with Spyder IDE for you to check the outputted images
directly.

Additional Libraries needed: matplotlib, numpy.

# Input 
The data generation variables are in line 41. You might want to adjust initialization variables on line 68. 
The default dummy values of the mean here is 3 and 7 respectively.

# Output
Algorithm will output a series of PNGs (or a series of images that can be seen using Spyder/IPython for each 
iteration.
Mean of each cluster are shown using vertical dotted lines.
Note that in the first iterations the means are off. As the iterations proceed the mean are getting better
and approaching true values.
The upper blue/red "bar" indicates the membership degrees for each datapoint. There is color in between red
and blue, indicates that the points there are having transition and the responsibility is shared between two
clusters.


![alt text](https://github.com/adewandaru/EM/blob/master/Webp.net-gifmaker.gif)
