# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example
# a =3
# b = 5
# Print the following:
#
# 8
# -2
# 15
#
# Input Format
#
# The first line contains the first integer, .
# The second line contains the second integer, .
#
# Constraints
#
# 1 <= a <= 10^10
# 1 <= b <= 10^10
#
# Output Format
#
# Print the three lines as explained above.
#
# Sample Input 0
#
# 3
# 2
#
# Sample Output 0
#
# 5
# 1
# 6
#
# Explanation 0
#
# 3 + 2 -> 5
# 3 - 2 -> 1
# 3 * 2 -> 6
###########################################################################################

a = int(input())
b = int(input())

sum = a + b
minus = a - b
multi = a * b
print(sum)
print(minus)
print(multi)

########################################################################
# You have earned 10.00 points!