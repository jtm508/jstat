Fisher Exact P-Values
=====================

This submodule is based on Chapter 5 of `Causal Inference For Statistics, Social, And Biomedical Sciences 
<https://www.amazon.com/Causal-Inference-Statistics-Biomedical-Sciences/dp/0521885884>`_. 

We consider a binary treatment, :math:`W_{i}\in\{0,1\}` for each unit :math:`i`. Under the potential outcomes framework, :math:`Y_{i}(0)` 
denotes :math:`i`'s outcome when :math:`W_{i}=0` and :math:`Y_{i}(1)` denotes :math:`i`'s outcomes when :math:`W_{i}=1`. We observe 
:math:`Y_{i}^{\text{obs}}\equiv Y_{i}(W_{i})`.
 
Fisher Exact P-Values (FEP) are non-parametric tests for the sharp null hypothesis. That is, the hypothesis the treatment effect is exactly
zero for each unit:

:math:`H_{0}:\, Y_{i}(0)=Y_{i}(1)\,\forall i`.

FEP's are computed by comparing a test statistic :math:`T(\mathbf{W})` under various assignment vectors, :math:`\mathbf{W}=\{W_{1},\dots,W_{n})`. 
Under the null hypothesis, we can impute :math:`Y_{i}(1-W_{i})` by setting it equal to :math:`Y_{i}(W_{i})` for each :math:`i`. The :math:`p`
value is computed as :math:`p=\frac{1}{K}\sum_{\mathbf{W}'}\mathbf{1}\left[T(\mathbf{W}^{\text{obs}})\le T(\mathbf{W}')\right]` where :math:`K` is the number 
of possible assignment mechanisms. FEP's are computed using :py:func:`jstat.fisher_exact.fisher_exact_p`.

In practice, :math:`K` can be too large to compute. We can approximate :math:`p` in such cases by randomly sampling assignment vectors and finding 
the proportion which yield larger test statistics than the test statistic under the observed assignment vector. The numw parameter in
:py:func:`jstat.fisher_exact.fisher_exact_p` allows users to to sample numw assignment vectors to approximate the p-value.
 
Test statistics
---------------
The following test statistcs are currently available for use:

:py:func:`jstat.fisher_exact.t_mean_diff`: 

	:math:`T(\mathbf{W},\mathbf{Y}^{\text{obs}})=\left|\bar{Y}_{t}^{\text{obs}}-\bar{Y}_{c}^{\text{obs}}\right|`
 
:py:func:`jstat.fisher_exact.t_median_diff`: 

	:math:`T(\mathbf{W},\mathbf{Y}^{\text{obs}})=\left|\text{med}\left(Y_{t}^{\text{obs}}\right)-\text{med}\left(Y_{c}^{\text{obs}}\right)\right|`
 