import numpy as np
from scipy.special import comb
from itertools import product


#To do:
# Add more test statistics

def t_mean_diff(Y,W,c=0):
    Y_t = np.mean(Y[W==1])
    Y_c = np.mean(Y[W==0])
    return np.abs(Y_t - Y_c)
	
def t_median_diff(Y,W,c=0):
    Y_t = np.median(Y[W==1]-c)
    Y_c = np.median(Y[W==0])
    return np.abs(Y_t - Y_c)
	
def fisher_exact_p(Y,W,T_function=t_mean_diff,numw=None,**kwargs):
    #number of units receiving treatment
    sumw = sum(W)
    #length of assignment vector (e.g. sample size)
    lenw = len(W)
    
    if not numw:
        #number of possible assignment vectors
        numw = int(comb(lenw,sumw))
    
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
    Parameters
    ----------
    N : Length of assignments vecotr
    K : Number of treated units
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
        
    if force_assignment is not None and list(np.where(force_assignment == 1)[0]) not in w_list:
        W[0] = force_assignment
        
    return W	