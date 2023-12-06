# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
#
# Example
#
# x = 1
# y = 1
# z = 2
# n = 3
#
# All permutations of [i, j, k] are:
#
# [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]]
#
# Print an array of the elements that do not sum to n = 3.
#
# [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]]
#
# Input Format
#
# Four integers x,y,z and n, each on a separate line.
#
# Constraints
#
# Print the list in lexicographic increasing order.
#
# Sample Input 0
#
# 1
# 1
# 1
# 2
#
# Sample Output 0
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#
# Explanation 0
#
# Each variable  and  will have values of 0 or 1. All permutations of lists in the form
# [i,j,k] = [[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]].
#
# Remove all arrays that sum to n = 2 to leave only the valid permutations.
#
# Sample Input 1
#
# 2
# 2
# 2
# 2
#
# Sample Output 1
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1],
# [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2],
# [2, 2, 0], [2, 2, 1], [2, 2, 2]]
#  [7 8 9]]
########################################################################################################################

x = int(input())
y = int(input())
z = int(input())
n = int(input())

my_list = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                elt = list(map(int, (i, j, k)))
                my_list.append(elt)

print(my_list)

########################################################################
# You have earned 10.00 points!