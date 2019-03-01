'''
Problem: https://www.hackerrank.com/challenges/new-year-chaos
Author: Noe

Description:
Complete the function minimumBribes in the editor below. It must print an integer representing the 
minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
'''

def minimumBribes(q):
    p = sorted(q)
    bribes ={}
    while p != q:
        for i in range(len(q)-1):
            if q[i] > q[i+1]:
                if q[i] in bribes and bribes[q[i]] > 1:
                    return "Too chaotic"
                elif q[i] in bribes:
                    bribes[q[i]] += 1
                else:
                    bribes[q[i]] = 1 
                q[i] += q[i+1]
                q[i+1] = q[i] - q[i+1]
                q[i] -= q[i+1]

    return sum([n for n in bribes.values()])

q = [1, 2, 5, 3, 7, 8, 6, 4] # should return 7
print(minimumBribes(q))