'''
Kata: https://www.codewars.com/kata/moving-zeros-to-the-end
runtime: 

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

ex: move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''
import uuid

def move_zeros(array):
    i = 0
    initial_size = len(array)

    while i < initial_size:
        if array[i] is 0 or (array[i] == float(0.0) and array[i] is not False):
            array[i] = uuid.uuid4()
            array.remove(array[i])
            array.append(0)
            i -= 1
            initial_size -= 1
        i += 1

    return array


# should equal [1,None,2,False,1,0]
b = [0.0,1,None,2,False,1]
# should equal ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]
e = ["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]

print(move_zeros(b))

print(move_zeros(e))
