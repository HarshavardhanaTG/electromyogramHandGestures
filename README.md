# Why is zero-shot decoding of EMG so difficult? 

One of the most vexing thing about multivaiate EMG signals is the significant shift in signal distribution across populations. In this paper, we explain why zero-shot learning is so difficult.

a. First, we show that EMG signals can be expressed as an approximate linear combination of a set of orthogonal axes. So, we have a set of basis vectors defining EMG signals from a given individual.
b. Next, we show that a set of basis vectors defining the EMG signals are different for different individuals.
c. This change of basis fundamentally limits zero-shot EMG learning. Whereas, few shot learning with a couple of labels is really easy. 

We provide data from `91` subjects here.
[Downlod our data](https://osf.io/3kzcb/).

The codes given here can be used to recreate results from our paper [Upper limb surface electromyography - geometry,
spectral characteristics, temporal evolution, and
demographic confounds](https://arxiv.org/pdf/2409.19939).


