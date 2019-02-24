'''
Problem: https://www.hackerrank.com/challenges/special-palindrome-again

Complete the substrCount function in the editor below. 
It should return an integer representing the number of special 
palindromic substrings that can be formed from the given string.
'''

import math

def substrCount(n, s):
    palindromeCount = n
    substringSize = 2
    while substringSize <= n:
        for i in range(n):
            sLength = len(s[i:i+substringSize])
            if s[i:i+substringSize].count(s[i]) == sLength:
                palindromeCount += 1

            if sLength > 2 and sLength % 2:
                leftSide = s[i:math.floor(i+substringSize/2)]
                rightSide = s[math.floor(i+substringSize/2)+1:i+substringSize]
                middleCharacter = s[math.floor(i+substringSize/2)]
                if leftSide == rightSide and middleCharacter != s[i]:
                    palindromeCount += 1
            
            if i+substringSize == n:
                break
        
        substringSize += 1

    return palindromeCount

print(substrCount(5, 'asasd'))