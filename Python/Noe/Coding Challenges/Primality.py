'''
Problem: https://www.hackerrank.com/challenges/ctci-big-o
Author: Noé
Function Description:
Complete the primality function in the editor below. It should return Prime if  is prime, or Not prime.
'''
import math


def primality(n):
    if n == 1:
        return 'Not prime'
    if n % 2 == 0 and n != 2:
        return 'Not prime'
    prime = 'Prime'
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if not n % i:
            prime = 'Not prime'
            break

    return prime


inputZ = [1,4,9,16]
inputA = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,907]
inputB = [1000000000,1000000001,1000000002,1000000003,1000000004,1000000005,1000000006,1000000007,1000000008,1000000009]

for i in range(len(inputA)):
    print("number {} is {}".format(inputA[i], primality(inputA[i])))

print("the end")


# testing stuff
import math
print(math.ceil(4/2))
