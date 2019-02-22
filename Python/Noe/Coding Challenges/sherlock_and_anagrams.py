'''
Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Function Description:
Complete the function sherlockAndAnagrams in the editor below. It must return an integer
that represents the number of anagrammatic pairs of substrings in .
'''


def sherlockAndAnagrams(s):
    anagramCount = 0
    substringSize = 1
    while substringSize < len(s):
        for i in range(len(s)):
            initialString = sorted(s[i:i+substringSize])
            for j in range(i+1, len(s)):
                if initialString == sorted(s[j:j+substringSize]):
                    anagramCount += 1

        substringSize += 1

    return anagramCount


print(sherlockAndAnagrams("abba")) # returns 4