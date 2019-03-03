'''
Problem: https://www.hackerrank.com/challenges/common-child
Author: Noé
Function Description:
Complete the commonChild function in the editor below. It should return the longest string which is a common child of the input strings.
'''
def commonChild(s1, s2):
    if len(s1) != len(s2):
        return 0
    maxLength = 0
    startingPoint = 0

    while len(s1) - startingPoint > maxLength:
        lastMatchIndex = 0
        currentChildLength = 0
        for i in range(startingPoint, len(s1)):
            for j in range(lastMatchIndex, len(s2)):
                if s1[i] == s2[j]:
                    currentChildLength += 1
                    lastMatchIndex = j+1
                    break
        if maxLength < currentChildLength:
            maxLength = currentChildLength

        startingPoint += 1
    
    return maxLength


a1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
a2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
print(commonChild(a1, a2)) # Should return 15


s1 = 'HARRY'
s2 = 'SALLY'

print(commonChild(s1, s2)) # Should return 2, 'AY' being the longest common child