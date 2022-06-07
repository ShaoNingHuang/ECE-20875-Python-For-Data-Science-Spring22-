import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Return fitted model parameters to the dataset at datapath for each choice in degrees.
# Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
# Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
# coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    # fill in
    # read the input file, assuming it has two columns, where each row is of the form [x y] as
    # in poly.txt.
    # iterate through each n in degrees, calling the feature_matrix and least_squares functions to solve
    # for the model parameters in each case. Append the result to paramFits each time.
    data=pd.read_csv(datapath,sep=' ',header=None)
    data.columns=["A","B"]
    for x in degrees:
        X=feature_matrix(data.A,x)
        b=least_squares(X, data.B)
        paramFits.append(b)
    newx=list(data.A)
    newx.sort()
    newy=list(data.B)
    newy.sort()
    plt.scatter(newx,newy,color='black',label='data')
    model1=[paramFits[0][0]*x+paramFits[0][1] for x in data.A]
    model1.sort()
    plt.plot(newx,model1,color='red',label='d1')
    model2=[paramFits[1][0]*x*x+paramFits[1][1]*x+paramFits[1][2] for x in data.A]
    model2.sort()
    plt.plot(newx,model2,color='blue',label='d2')
    model3=[paramFits[2][0]*x*x*x+paramFits[2][1]*x*x+paramFits[2][2]*x+paramFits[2][3] for x in data.A]
    model3.sort()
    plt.plot(newx,model3,color='green',label='d3')
    model4=[paramFits[3][0]*x*x*x*x+paramFits[3][1]*x*x*x+paramFits[3][2]*x*x+paramFits[3][3]*x+paramFits[3][4] for x in data.A]
    model4.sort()
    plt.plot(newx,model4,color='orange',label='d4')
    model5=[paramFits[4][0]*x*x*x*x*x+paramFits[4][1]*x*x*x*x+paramFits[4][2]*x*x*x+paramFits[4][3]*x*x+paramFits[4][4]*x+paramFits[4][5] for x in data.A]
    model5.sort()
    plt.plot(newx,model5,color='purple',label='d5')
    plt.legend(loc='best')
    plt.xlabel("x")
    plt.ylabel("y")
    x=2
    y=paramFits[2][0]*x*x*x+paramFits[2][1]*x*x+paramFits[2][2]*x+paramFits[2][3]
    print(y)
    plt.show()
    return paramFits


# Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
# samples in x.
# Input: x as a list of the independent variable samples, and d as an integer.
# Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
# for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):

    # fill in
    # There are several ways to write this function. The most efficient would be a nested list comprehension
    # which for each sample in x calculates x^d, x^(d-1), ..., x^0.
    X=[[l**z for z in range(d,-1,-1)]for l in x]
    return X


# Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
# Input: X as a list of features for each sample, and y as a list of target variable samples.
# Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    # fill in
    # Use the matrix algebra functions in numpy to solve the least squares equations. This can be done in just one line.
    B=np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),y)
    return B


if __name__ == "__main__":
    datapath = "poly.txt"
    degrees = [1,2,3,4,5]
    paramFits = main(datapath, degrees)
    print(paramFits)
