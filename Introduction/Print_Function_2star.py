# The included code stub will read an integer, n , from STDIN.
#
# Without using any string methods, try to print the following:
# 123...n
#
# Note that "" represents the consecutive values in between.
#
# Example
#
# n = 5
#
# Print the string 12345.
#
# Input Format
#
# The first line contains an integer n.
#
# Constraints
#
# 1 <= n <= 150
#
# Output Format
#
# Print the list of integers from 1 through n as a string, without spaces.
#
# Sample Input 0
#
# 3
#
# Sample Output 0
#
# 123
###########################################################################################

def print_number(number):
    for num in range(1, number + 1):
        print(num, end='')


numberInput = int(input())
print_number(numberInput)

########################################################################
# You have earned 20.00 points!
# Congrats!
# You have earned your 2nd star.
