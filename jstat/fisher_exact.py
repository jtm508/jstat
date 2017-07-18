from __future__ import division
import numpy as np
from scipy.special import comb
from itertools import product

#To do:
# Add more test statistics

def t_mean_diff(Y,W):
	'''
	Computes a test statistic for the sharp null hypothesis of no treatment effect based on differences in means.

	Parameters
	----------
	Y : numpy array
		Vector of outcomes.

	W : numpy array
		Assignment vector.

	Returns
	-------
	T : float
		Test statistic for difference in means under the sharp null hypothesis.
	'''
	Y_t = np.mean(Y[W==1])
	Y_c = np.mean(Y[W==0])
	T = np.abs(Y_t - Y_c)
	return T
	
def t_median_diff(Y,W):
	'''
	Computes a test statistic for the sharp null hypothesis of no treatment effect based on differences in medians.
	
	Parameters
	----------
	Y : numpy array
		Vector of outcomes.
	
	W : numpy array
		Assignment vector.
	
	Returns
	-------
	T : float
		Test statistic for difference in medians under the sharp null hypothesis.
	'''
	Y_t = np.median(Y[W==1])
	Y_c = np.median(Y[W==0])
	T = np.abs(Y_t - Y_c)
	return T
	
def fisher_exact_p(Y,W,T_function=t_mean_diff,force=False,numw=None,**kwargs):
	'''
	Computes a Fisher Exact P-value according to the test statistic defined by T_function

	Parameters
	----------
	Y : numpy array
		Vector of outcomes.

	W : numpy array
		Assignment vector.

	T_function : python function
		Function to compute a test statistic.
		
	force : boolean
		Set to True in order to force an exact p-value computation with over 1 million assignment vectors.

	numw : positive integer, optional
		Approximate the p-value based on a random sample of numw possible assignment vectors. use if (N_c+N_t)Choose(N_t) is large.

	**kwargs : variable types
		Arguments to pass into T_function.

	Returns
	-------
	p : float
		Fisher Exact P-Value.
	'''
	#number of units receiving treatment
	sumw = sum(W)
	#length of assignment vector (e.g. sample size)
	lenw = len(W)
	
	

	if not numw:
		#number of possible assignment vectors
		numw = int(comb(lenw,sumw))
		if force == False:
			assert numw < 1000000, "The number of assignment vectors is over one million. Continuing may cause you to run out of memory. Use the option force=True to continue. Use the numw option to approximate the p-value"

		#generator of assignment vectors
		assignments = product([0, 1], repeat=lenw)
	else:
		assignments = random_assignments(lenw,sumw,numw,force_assignment=W)
		print("Maximum standard error for p_value is {}.".format(1/(2*np.sqrt(numw))))


	#initialize storage
	T = np.empty(numw)

	#calculate t_stat for each assignment vector
	i = 0
	for w in list(assignments):
		if sum(w)==sumw: #only use assignment vectors with correct treatment/control sizes
			#save the index of the actual assignment vector
			if np.array_equal(w,W):
				W_index = i
			T[i] = T_function(Y,np.array(w),**kwargs)
			i+=1

	#T statistic for true assignment vector
	T_true = T[W_index]

	#p_value
	p = sum(T>=T_true) / len(T)

	return(p)
	
def random_assignments(N,K,rep=1,force_assignment=None):
    '''
	Samples assignment vectors without replacement to calculate Fisher Exact P-Values.
	
    Parameters
    ----------
    N : Positive Integer
	Length of assignments vector.
		
    K : Positive Integer
	Number of treated units.
		
	rep : Positive Integer
	Number of assignment vectors to calculate.
		
	force_assignment : list
	If used, this will the function will ensure force_assignment is in the list of sampled vectors.
	This is meant to take on the value of the true assignment vector.
		
	Returns
	-------
	W : numpy array
	Each row is a distinct assignment vector drawn randomly from the population of assignment vectors.
    '''
    #initialize assignment matrix
    W = np.zeros([rep,N],dtype=int)
    #initalize list of assigment vector indexes
    w_list = [[]] * rep
    
    w=[]    
    for i in range(rep):
        #draw a NEW list of indexes
        while w in w_list:
            w = list(set(np.random.choice(np.arange(N),K,replace=False)))
        w_list[i] = w
        W[[i,w]] = 1
    
	#force the actual assignment vector into a list.
    if force_assignment is not None and list(np.where(force_assignment == 1)[0]) not in w_list:
        W[0] = force_assignment
        
    return W	