import numpy as np

#file for generating data to test the functions

def gen_constant_treatment_effect(N,mu,c,p):
	'''
	Generate data with no covariates, binary treatments, and a constant treatment effect. The outcomes are
	independently normally distributed with variance 1.

	Parameters
	----------
	N : Positive Integer
		Mumber of observations in the dataset.

	mu : float
		The average outcome for units which do not receive the treatment.
		
	c : float
		The treatment effect
		
	p : float between 0 and 1
		The proportion of units which receive the treatment.

	Returns
	-------
	Y : numpy array
		Vector of outcomes.
		
	W : numpy array
		Assignment vector
	'''
	W = np.random.binomial(1,p,N)
	epsilon = np.random.normal(0,1,N)
	Y = mu + W*c + epsilon
	return Y, W
	
def gen_average_treatment_effect(N,mu,c,p):
	'''
	Generate data with no covariates, binary treatments, and a heterogeneous treatment effect. The outcomes are
	independently normally distributed with variance 1. Treatment effects also have variance 1.
	
	Parameters
	----------
	N : Positive Integer
		Mumber of observations in the dataset.
	
	mu : float
		The average outcome for units which do not receive the treatment.
		
	c : float
		The average treatment effect
		
	p : float between 0 and 1
		The proportion of units which receive the treatment.
	
	Returns
	-------
	Y : numpy array
		Vector of outcomes.
		
	W : numpy array
		Assignment vector
	'''
	W = np.random.binomial(1,p,N)
	epsilon = np.random.normal(0,1,N)
	treatment_effect = np.random.normal(c,1,N)
	Y = mu + W*treatment_effect + epsilon
	return Y, W