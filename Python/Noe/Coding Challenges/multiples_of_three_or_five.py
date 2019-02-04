'''
Kata Difficulty: 6
runtime: O(N)

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
'''
class multiples:
    def multiple_sum(self, n):
        return sum(i for i in range(0, n) if not i % 3 or not i % 5)


cl = multiples()
print(cl.multiple_sum(10))