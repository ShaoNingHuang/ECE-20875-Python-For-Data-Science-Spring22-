import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# import or paste dataset here
myfile=open('engagement_0.txt')
data1=myfile.readlines()
myfile.close()
data1=[float(x) for x in data1]
myfile=open('engagement_1.txt')
data2=myfile.readlines()
myfile.close()
data2=[float(x) for x in data2]

# code for question 2
print('Problem 2 Answers:')
# code below this line
sample_size1=len(data2)
print(sample_size1)
sample_mean1=np.mean(data2)
print(sample_mean1)
std_error=np.std(data2,ddof=1)/(np.sqrt(sample_size1))
print(std_error)
z_score=(sample_mean1-0.75)/std_error
print(z_score)
pvalue=2*stats.norm.cdf(-abs(z_score))
print(pvalue)
# code for question 3
print('Problem 3 Answers:')
# code below this line
zscore=stats.norm.ppf(0.05)
newstderror=(sample_mean1-0.75)/zscore
print(newstderror)
minsamplesize=(int)((np.std(data2,ddof=1)**2)/newstderror**2)
print(minsamplesize)
# code for question 5
print('Problem 5 Answers:')
# code below this line
samplesize0=len(data1)
print(samplesize0)
print(sample_size1)
samplemean0=np.mean(data1)
print(samplemean0)
print(sample_mean1)
stderror=np.sqrt((np.std(data1,ddof=1)**2)/len(data1)+(np.std(data2,ddof=1)**2)/len(data2))
print(stderror)

zscore=(samplemean0-sample_mean1)/stderror
print(zscore)
p_value=2*stats.norm.cdf(-abs(zscore))
print(p_value)