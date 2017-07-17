import numpy as np

def gen_constant_treatment_effect(N,mu,c,p):
    W = np.random.binomial(1,p,N)
    epsilon = np.random.normal(0,1,N)
    Y = mu + W*c + epsilon
    return Y, W
	
def gen_average_treatment_effect(N,mu,c,p):
    W = np.random.binomial(1,p,N)
    epsilon = np.random.normal(0,1,N)
    treatment_effect = np.random.normal(c,1,N)
    Y = mu + W*treatment_effect + epsilon
    return Y, W