'''
Kata Link: https://www.codewars.com/kata/square-into-squares-protect-trees

Problem:
Given a positive integral number n, return a strictly increasing
sequence (list/array/string depending on the language) of numbers,
so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return the result with the largest possible values.
decompose(4) => None
decompose(5) => [3,4]
decompose(8) => None
decompose(11) => [1,2,4,10]
decompose(50) => [1,3,5,8,49]
'''



def decompose(n):
    k = n-1
    current = n-1
    sum = 0
    digits = []
    
    while sum < pow(n, 2):
        if current == 1:
            return None

        if sum+pow(k, 2) <= pow(n, 2):
            digits.insert(0, k)
            print(digits)
            sum += pow(k, 2)
            k -= 1
        elif sum+pow(k, 2) > pow(n, 2) and current != 1:
            # do something here?
            tmp = digits
        elif sum+pow(k, 2) > pow(n, 2) and current == 1:
            digits = []
            sum = 0
            current -= 1
            k = current
        else:
            k -= 1

    return digits


print(decompose(11))
print(decompose(50))

