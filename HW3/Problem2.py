import scipy.stats as stats
import matplotlib.pyplot as plt
import math
from helper import *

def get_coordinates(data, each_dist):
    # Part B
    """
    :param: np.ndarray, str
    :return: np.ndarray, np.ndarray
    """
    # Your code starts here...
    val1,val2=stats.probplot(data,dist=each_dist)
    thistuple=(val1)
    
    return thistuple


def calculate_distance(x, y):
    # Part B

    """
    :param: float, float
    :return: float
    """
    # Your code starts here...
    distance=math.sqrt(((x-((x+y)/2))**2)+((y-((x+y)/2))**2))
    
    return distance


def find_dist(sum_err, dists):
    # Part B
    """
    :param: list[float], list[str]
    :return: str, float
    """
    # Your code starts here...
    num=min(sum_err)
    index=0
    for x in range(0,len(sum_err)):
        if sum_err[x]==num:
            index=x
            break
    thistuple=(dists[index],num)
    
    return thistuple    


def main(data_file):
    """
        Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return 'norm',0.32)
    :param: *.csv file name (str)
    :return: str, float
    """
    # Part B
    data = get_data(data_file)
    dists = ("norm", "expon", "uniform", "wald")
    sum_err = [0] * 4
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist)
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y)
    return find_dist(sum_err, dists)


if __name__ == "__main__":
    for each_dataset in [
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
    ]:
        print(main(each_dataset))
