"""
#Brute Force
n = int(input("Enter the number\n"))
num = n
result = [] #list
for i in range(1, num+1):
    if num % i == 0:
        result.append(i) #O(1)
print(result)

#TC = O(n), where n is the number
#SC = O(k), where k is the number of factors
"""

"""
#Optimized Solution 
# For any number, the factors are there between 1 to half of the number
# if number is 10, then from 1-5 there are divisors but after 5 there are no divisors till the number 10 itself
n = int(input("Enter the number\n"))
num = n
limit = n // 2
result = [] #list
for i in range(1, limit+1):
    if num % i == 0:
        result.append(i) #O(1)
result.append(n)
print(result)

#TC = O(n/2) almost equal to O(n) after removing constant, where n is the number
#SC = O(k), where k is the number of factors
"""

#Most Optimal Solution
#The square root of number can be done
from math import *
n=int(input("Enter the number\n"))
num = n
result = []
SQROOT = sqrt(num)
for i in range(1, int(SQROOT+1)):
    if num % i == 0: #this calculates from 1 to the sqroot of the number
        result.append(i)
        if num // i != i: #this gives the dividend
            result.append(num // i)
print(result)
result.sort() #O(n logn )
print(result) #if asked to return in sorted manner

#TC = O(sqrt(n)) + O(n log n), if no sorting -> O(sqrt(n))
#SC = O(k), where k is the number of factors