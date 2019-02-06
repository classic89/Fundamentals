'''
Kata(6): https://www.codewars.com/kata/persistent-bugger
runtime: O(N) N being the number of digits

Write a function, persistence, that takes in a positive parameter num
and returns its multiplicative persistence, which is the number of times
you must multiply the digits in num until you reach a single digit.
'''

def persistence(n, iterations=0):
    if n < 10:
        return iterations
    l = list(str(n))
    result = 1
    
    for i in range(0, len(l)):
        result *= int(l[i])
    
    return persistence(result, iterations+1)


print(persistence(39)) # returns 3