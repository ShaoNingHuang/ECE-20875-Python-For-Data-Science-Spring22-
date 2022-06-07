import os
import sys
import numpy as np
from cluster import *
from point import *
from kmeans import *
from gmm import *


# test cases for point.py
data_point1 = np.array([[2.0, 5.0], [-1.0, 3.0]])
data_point2 = np.array([[1.0, 2.0, 5.0], [3.0, 4.0, 8.0], [0.0, -6.0, -2.0], [-1.0, -1.0, 4.0]])
data_point3 = np.array([[1.0, 2.0, 5.0, 9.0], [7.0, -7.0, 3.0, 20.0], [2.0, 2.0, 1.0, 1.0]])
tc1_sol_1 = makePointList(data_point1)
print('Test Case 1 Output: ' + str(tc1_sol_1))
tc2_sol = tc1_sol_1[0].distFrom(tc1_sol_1[1])
tc2_sol = round(tc2_sol, 2)
print('Test Case 2 Output: ' + str(tc2_sol))
tc3_sol_1 = makePointList(data_point2)
print('Test Case 3 Output: ' + str(tc3_sol_1))
tc4_sol = tc3_sol_1[0].distFrom(tc3_sol_1[1])
tc4_sol = round(tc4_sol, 2)
print('Test Case 4 Output: ' + str(tc4_sol))
tc5_sol_1 = makePointList(data_point3)
print('Test Case 5 Output: ' + str(tc5_sol_1))
tc6_sol = tc5_sol_1[0].distFrom(tc5_sol_1[1])
tc6_sol = round(tc6_sol, 2)
print('Test Case 6 Output: ' + str(tc6_sol))

# test cases for cluster.py
p1 = Point([-1.0, 3.5, 4.0])
p2 = Point([0.0, -2.0, 3.0])
c = Cluster(Point([1.0, 2.5, 9.0]))
c.addPoint(p1)
c.addPoint(p2)
tc7_sol = c
print('Test Case 7 Output: ' + str(tc7_sol))
tc8_sol = c.avgDistance
tc8_sol = round(tc8_sol, 2)
print('Test Case 8 Output: ' + str(tc8_sol))

p3 = Point([6.5, 7.2, 9.0, -1.0])
p4 = Point([0.0, -2.0, 3.0, -5.5])
p5 = Point([-4.5, -6.0, 8.0, -2.5])
e = Cluster(Point([0.0, 0.0, 0.0, 0.0]))
e.addPoint(p3)
e.addPoint(p4)
e.addPoint(p5)
tc9_sol = e
print('Test Case 9 Output: ' + str(tc9_sol))
tc10_sol = e.avgDistance
tc10_sol = round(tc10_sol, 2)
print('Test Case 10 Output: ' + str(tc10_sol))

p6 = Point([1.5])
p7 = Point([2.5])
p8 = Point([3.5])
h = Cluster(Point([0.0]))
h.addPoint(p6)
h.addPoint(p7)
h.addPoint(p8)
tc11_sol = h
print('Test Case 11 Output: ' + str(tc11_sol))
tc12_sol = h.avgDistance
tc12_sol = round(tc12_sol, 2)
print('Test Case 12 Output: ' + str(tc12_sol))


# test cases for kmeans.py
data_kmeans1 = np.array([[1, 2, 3], [1, 2, 1], [1, 1, 1], [3, 1, 3], [0, 0, 0]], dtype=float)
centers1 = np.array([[0, 0, 1], [1, 1, 2]], dtype=float)
tc13_sol = kmeans(data_kmeans1, centers1)
print('Test Case 13 Output: ' + str(tc13_sol))

data_kmeans2 = np.array([[1, 1], [2, 2], [4, 4], [6, 6], [0, 0]], dtype=float)
centers2 = np.array([[0, 0], [2, 2]], dtype=float)
tc14_sol = kmeans(data_kmeans2, centers2)
print('Test Case 14 Output: ' + str(tc14_sol))

data_kmeans3 = np.array([[0.0, 1.0, -2.0], [-5.0, 5.0, 6.0], [-10.0, -5.0, -1.0], [5.0, 5.0, -9.0], [3.0, -1.0, -4.0], [6.0, 7.0, -8.0], [8.0, -3.0, 4.0]], dtype=float)
centers3 = np.array([[0, 0, 1], [1, 1, 2], [-2, 2, 2]], dtype=float)
tc15_sol = kmeans(data_kmeans3, centers3)
print('Test Case 15 Output: ' + str(tc15_sol))

# test cases for gaus_mixture function
X1 = np.genfromtxt('gmm_tc1_ans4.csv', delimiter=',')
X1 = np.reshape(X1, (200, 1))
tc16_sol = gaus_mixture(data=X1, n_components=[2, 3, 4, 6, 7, 8])
print('Test Case 16 Output: ' + str(tc16_sol))

X2 = np.genfromtxt('gmm_tc2_ans2.csv', delimiter=',')
X2 = np.reshape(X2, (100, 1))
tc17_sol = gaus_mixture(data=X2, n_components=[2, 7, 8])
print('Test Case 17 Output: ' + str(tc17_sol))
