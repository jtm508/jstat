Neyman's Repeated Sampling Approach
===================================

This submodule is based on Chapter 6 of `Causal Inference For Statistics, Social, And Biomedical Sciences 
<https://www.amazon.com/Causal-Inference-Statistics-Biomedical-Sciences/dp/0521885884>`_. 

Neyman's approach to randomized experiments aims to estimate the average treatment effect: :math:`E[Y_{i}(1)-Y_{i}(0)]`.
The functions below allow the user to estimate the average treatment effect, estimate the sampling variance, construct
confidence intervals, and test hypotheses.

Functions
---------
:py:func:`jstat.neyman.randomized_ate`: 

	This function returns an unbiased estimate of the average treatment effect: :math:`\bar{Y}_{t}^{\text{obs}}-\bar{Y}_{c}^{\text{obs}}`.
	
	The sampling variance of this estimator is equal to :math:`\frac{S_{c}^{2}}{N_{c}}+\frac{S_{t}^{2}}{N_{t}}-\frac{S_{tc}^{2}}{N}`
	where :math:`S_{c}^{2}` and :math:`S_{t}^{2}` are the variances of :math:`Y_{i}(0)` and :math:`Y_{i}(1)` respectively, and 
	:math:`S_{tc}^{2}` is the variance of the unit-level treatment effects. The challenge is that :math:`S_{tc}^{2}` is
	impossible to estimate with data from the experiment. The functions below attempt to solve this problem.
	
:py:func:`jstat.neyman.sampling_variance_neyman`: 

	Under constant treatment effects, this function produces an ubiased estimator of the sampling variance for the sample
	average treatment effect. With heterogeneous treatment effects, the estimate will overstate the variance. 
	
	However, this estimator is generally used because it provides an unbiased estimate of the population level average treatment 
	effect, which is typically what the researcher is after.
	
:py:func:`jstat.neyman.ate_sampling_variance_correlated`: 

	If the potential outcomes are perfectly correlated, this provides an unbiased etimate of the samplig variance. If the 
	correlation is not perfect, the variance is again upwardly biased, but less so than sampling_variance_neyman(). 
	
:py:func:`jstat.neyman.cte_sampling_variance`: 

	This estimator exploits the fact that :math:`S_{t}^{2}=S_{c}^{2}` if the treatment effect is constant. If treatment effects
	are constant, this estimator is preferred to the previous two. Otherwise it should not be used.
	
:py:func:`jstat.neyman.ate_confidence_interval`: 

	This function produces a :math:`1-\alpha` % confidence interval for the average treatment effect estimate. The user must
	supply an estimate of the sampling variance obtained from one of the previous functions. The confidence interval is
	justified in large samples by the Central Limit Theorem, but is fairly reliable in small samples as well. 
	
:py:func:`jstat.neyman.t_stat`: 

	The t-statistic produced by this function tests the null hypothesis that the average treatment effect is equal to zero.
	The user must supply a sampling variance from one of the previous functions. A p-value is also returned.