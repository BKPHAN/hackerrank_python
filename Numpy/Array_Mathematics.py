# Basic mathematical functions operate element-wise on arrays.
# They are available both as operator overloads and as functions in the NumPy module.
#
# import numpy
#
# a = numpy.array([1,2,3,4], float)
# b = numpy.array([5,6,7,8], float)
#
# print a + b                     #[  6.   8.  10.  12.]
# print numpy.add(a, b)           #[  6.   8.  10.  12.]
#
# print a - b                     #[-4. -4. -4. -4.]
# print numpy.subtract(a, b)      #[-4. -4. -4. -4.]
#
# print a * b                     #[  5.  12.  21.  32.]
# print numpy.multiply(a, b)      #[  5.  12.  21.  32.]
#
# print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
# print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]
#
# print a % b                     #[ 1.  2.  3.  4.]
# print numpy.mod(a, b)           #[ 1.  2.  3.  4.]
#
# print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
# print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
#
# ----------------------------------------------------------------------------------------------------------------------
#
# Task
#
# You are given two integer arrays, A and B of dimensions NxM.
# Your task is to perform the following operations:
#
# Add (A + B)
# Subtract (A - B)
# Multiply (A * B)
# Integer Division (A / B)
# Mod (A % B)
# Power (A ** B)
#
# Note
#
# There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
#
# Input Format
#
# The first line contains two space separated integers, N and M.
# The next N lines contains M space separated integers of array A.
# The following N lines contains M space separated integers of array B.
#
# Output Format
#
# Print the result of each operation in the given order under Task.
#
# Sample Input
#
# 1 4
# 1 2 3 4
# 5 6 7 8
# Sample Output
#
# [[ 6  8 10 12]]
# [[-4 -4 -4 -4]]
# [[ 5 12 21 32]]
# [[0 0 0 0]]
# [[1 2 3 4]]
# [[    1    64  2187 65536]]
# Use // for division in Python 3.
########################################################################################################################
import numpy as np

N, M = map(int, input().split())
A = []
B = []
for i in range(N):
    elt = list(map(int, input().split()))
    A.append(elt)
A = np.array(A, int)
for i in range(N):
    elt = list(map(int, input().split()))
    B.append(elt)
B = np.array(B, int)

# Examples 1:

add_array = np.add(A, B)
subtract_array = np.subtract(A, B)
multiply_array = np.multiply(A, B)
division_array = np.divide(A, B).astype(int)
mod_array = np.mod(A, B)
power_array = np.power(A, B)
# Examples 2:

add_array = A + B
subtract_array = A - B
multiply_array = A * B
division_array = A // B # (A / B).astype(int)
mod_array = A % B
power_array = A ** B

print(add_array, subtract_array, multiply_array, division_array, mod_array, power_array, sep='\n')

########################################################################
# You have earned 20.00 points!
