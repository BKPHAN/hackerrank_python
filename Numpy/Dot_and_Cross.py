# dot
#
# The dot tool returns the dot product of two arrays.
#
# import numpy
#
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])
#
# print numpy.dot(A, B)       #Output : 11
#
# cross
#
# The cross tool returns the cross product of two arrays.
#
# import numpy
#
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])
#
# print numpy.cross(A, B)     #Output : -2
#
# -----------------------------------------------------------------------------------------------------------------------
#
# Task
#
# You are given two arrays A and B. Both have dimensions of NxN.
# Your task is to compute their matrix product.
#
# Input Format
#
# The first line contains the integer N.
# The next N lines contains N space separated integers of array A.
# The following N lines contains N space separated integers of array B.
#
# Output Format
#
# Print the matrix multiplication of A and B.
#
# Sample Input
#
# 2
# 1 2
# 3 4
# 1 2
# 3 4
# Sample Output
#
# [[ 7 10]
#  [15 22]]
########################################################################################################################
import numpy as np

N = int(input())
A = []
B = []
for i in range(N):
    elt = list(map(int, input().split()))
    A.append(elt)

for i in range(N):
    elt = list(map(int, input().split()))
    B.append(elt)
# -----------------------------------------------------------------------------------------------------------------------
# Example 1:
C = np.dot(A, B)
# Example 2:
C = np.matmul(A, B)
print(C)

########################################################################
# You have earned 20.00 points!
