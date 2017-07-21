import numpy as np
from scipy.stats import norm

def randomized_ate(Y,W):
	'''
	Computes an unbiased estimator of the average treatment effect when units are randomly assigned to
	the treatment and control groups.

	Parameters
	----------
	Y : numpy array
		Vector of outcomes.

	W : numpy array
		Assignment vector.

	Returns
	-------
	ATE : float
		Estimate of the average treatment effect.
	'''
    Y_t = np.mean(Y[W==1])
    Y_c = np.mean(Y[W==0])
    ATE = Y_t - Y_c
    return ATE
	
def sampling_variance_neyman(Y,W):
	'''
	Computes an ubiased estimator of the sampling variance of randomized_ate under constant treatment effects.
	Note that if treatment effects are heterogeneous, this will not yield an unbiased estimate.

	Parameters
	----------
	Y : numpy array
		Vector of outcomes.

	W : numpy array
		Assignment vector.

	Returns
	-------
	V : float
		Estimate of the sampling variance of the the estimator defined by randomized_ate.
	'''
    #treatment and control sample sizes
    N_c = sum(W==0)
    N_t = sum(W==1)
    
    Y_c_bar = np.mean(Y[W==0]) #average response of control group
    s2_c = sum((Y[W==0]-Y_c_bar)**2)/(N_c-1) #variance of Y_i(0)
    
    Y_t_bar = np.mean(Y[W==1]) #average response of treatment group
    s2_t = sum((Y[W==1]-Y_t_bar)**2)/(N_t-1) #variance of Y_i(1)
    
    V = s2_c/N_c + s2_t/N_t
    return V
	
def ate_sampling_variance_correlated(Y,W):
    '''
	Computes an ubiased estimator of the sampling variance of randomized_ate assuming the potential outcomes are perfectly correlated.
    If the true correlation is less than 1, the variance is upwardly biased.

	Parameters
	----------
	Y : numpy array
		Vector of outcomes.

	W : numpy array
		Assignment vector.

	Returns
	-------
	V : float
		Estimate of the sampling variance of the the estimator defined by randomized_ate.
    '''
    #treatment and control sample sizes
    N_c = sum(W==0)
    N_t = sum(W==1)
    N = len(W)
    
    Y_c_bar = np.mean(Y[W==0]) #average response of control group
    s2_c = sum((Y[W==0]-Y_c_bar)**2)/(N_c-1) #variance of Y_i(0)
    s_c = np.sqrt(s2_c)
    
    Y_t_bar = np.mean(Y[W==1]) #average response of treatment group
    s2_t = sum((Y[W==1]-Y_t_bar)**2)/(N_t-1) #variance of Y_i(1)
    s_t = np.sqrt(s2_t)
    
    V = s2_c/N_c + s2_t/N_t - (s_t-s_c)**2/N
    return V
	
def cte_sampling_variance(Y,W):
    '''
	Computes an ubiased estimator of the sampling variance of randomized_ate under constant treatment effects.
	This estimator is preferred to Neyman's estimator if the treatment effect is constant and the treatment effect 
	is defined over the sample population rather than the super population.

	Parameters
	----------
	Y : numpy array
		Vector of outcomes.

	W : numpy array
		Assignment vector.

	Returns
	-------
	V : float
		Estimate of the sampling variance of the the estimator defined by randomized_ate
    '''
    Y_c_bar = np.mean(Y[W==0]) #average response of control group  
    Y_t_bar = np.mean(Y[W==1]) #average response of treatment group
    
    #treatment and control sample sizes
    N_c = sum(W==0)
    N_t = sum(W==1)
    N = len(W)
    
    s2 = (sum((Y[W==0]-Y_c_bar)**2)+sum((Y[W==1]-Y_c_bar)**2))/(N-2)
    
    V = s2*(1/N_c + 1/N_t)
    return V
	
def ate_confidence_interval(tao,V,alpha):
    '''
	Computes a 1-alpha % confidence interval for tao, an estimate of the average treatment effect.
	
    Parameters
    ----------
    tao : An estimate of the average treatment effect
	
    V : An estimate of the sampling variance of tao
	
    alpha : The function computes (1-alpha)% confidence interval
	
	Returns
	-------
	CI : list
		A list containing the lower and uppoer bound of a 1-alpha % confidence interval.
    '''
    #compute z scores using standard normal distribution quantiles
    z1 = norm.ppf(alpha/2) 	 #zscore: z_alpha/2
    z2 = norm.ppf(1-alpha/2) #zscore: z_(1-alpha/2)
    
    CI = [tao + z1 * np.sqrt(V), tao + z2 * np.sqrt(V)]
	return CI
	
def t_stat(Y,W,V):
    '''
	Computes a test statistic and p-value for the null hypothesis that the ATE equals 0.
	
    Parameters
    ----------
    Y : Observed outcomes
	
    W : Assignment vector
	
    V : Estimate of sampling variance of ATE, e.g. from sampling_variance_neyman()

	Returns
	-------
	t : float
		A list containing the lower and uppoer bound of a 1-alpha % confidence interval.
	
	p : float
		associated p-value for t, based on the normal approximation to t.
    '''
    t = average_treatment_effect(Y,W)/np.sqrt(V)
	p = 2*(1-norm.cdf(abs(t)))
    return t, p