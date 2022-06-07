import numpy as np
import matplotlib.pyplot as plt
import sys


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities
    :param hist: a numpy ndarray object
    :return: list
    """
    length=len(hist)
    thislist=length*[0]
    num=sum(hist)
    for x in range (0,length):
        thislist[x]=hist[x]/num
    return thislist


def compute_j(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates compute_j for one bin width
    :param histo: list
    :param width: float
    :return: float
    """
    m=sum(histo)
    thislist=norm_histogram(histo)
    for x in range (0,len(thislist)):
        thislist[x]=thislist[x]*thislist[x]
    sumofprob=sum(thislist)
    J=(2/((m-1)*width))-((m+1)/((m-1)*width))*sumofprob
    return J


def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    num=max_bins-min_bins+1
    thislist=num*[0]
    for x,y in zip(range(0,num),range(min_bins,max_bins+1)):
        thislist[x]=compute_j(plt.hist(data,y,(minimum,maximum))[0],(maximum-minimum)/y)

    return thislist    
        
        
    
    


def find_min(l):
    """
    takes a list of numbers and returns the mean of the three smallest number in that list and their index.
    return as a tuple i.e. (the_mean_of_the_3_smallest_values,[list_of_the_3_smallest_values])
    For example:
        A list(l) is [14,27,15,49,23,41,147]
        The you should return ((14+15+23)/3,[0,2,4])

    :param l: list
    :return: tuple
    """
    index1=0
    index2=0
    index3=0
    num1=0
    num2=0
    num3=0
    num1=min(l)
    for x in range(0,len(l)):
        if l[x]==num1:
            index1=x
            l[x]=sys.float_info.max
        else:
            continue
    #print(num1,index1,l[index1])  
    num2=min(l)
    for x in range(0,len(l)):
        if l[x]==num2:
            index2=x
            l[x]=sys.float_info.max
        else:
            continue
    #print(num2,index2,l[index2])
    num3=min(l)
    for x in range(0,len(l)):
        if l[x]==num3:
            index3=x
            l[x]=sys.float_info.max
        else:
            continue
    #print(num3,index3,l[index3])
    
    thistuple=((num1+num2+num3)/3,[index1,index2,index3])
    return thistuple
   


if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
