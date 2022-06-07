import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data=[3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]

# code for question 1
print('Problem 1 Answers:')
# code below this line
samplemean=np.mean(data)
print(samplemean)
stderror=np.std(data,ddof=1)/np.sqrt(len(data))
print(stderror)
tscore=stats.t.ppf(1-(1-0.9)/2,len(data)-1)
print(tscore)
l=samplemean-stderror*tscore
u=samplemean+stderror*tscore
print([l,u])



# code for question 2
print('Problem 2 Answers:')
# code below this line
tscore=stats.t.ppf(1-(1-0.95)/2,len(data)-1)
print(tscore)
l=(samplemean-stderror*tscore)
u=(samplemean+stderror*tscore)
print([l,u])

# code for question 3
print('Problem 3 Answers:')
# code below this line
std_error=15.836/np.sqrt(len(data))
print(std_error)
zc=stats.norm.ppf(1-(1-0.95)/2)
print(zc)
l=samplemean-std_error*zc
u=samplemean+std_error*zc
print([l,u])
# code for question 4
print('Problem 4 Answers:')
# code below this line
tscore=samplemean/stderror
p=stats.t.cdf(tscore,len(data)-1)
print(p)
