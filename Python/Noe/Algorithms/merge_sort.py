# import unittest as test

def merge_sort(array):
    if len(array) < 2:
        return array

    left_array = merge_sort(array[:int(len(array)/2)])
    right_array = merge_sort(array[int(len(array)/2):])

    return merge(left_array, right_array)


def merge(left_array, right_array):
    sorted_array = []

    while len(left_array) and len(right_array):
        if left_array[0] > right_array[0]:
            sorted_array.append(right_array[0])
            right_array.pop(0)
        else:
            sorted_array.append(left_array[0])
            left_array.pop(0)

    sorted_array += left_array + right_array

    return sorted_array


# input variables
unsorted_array = [5,3,7,34,7,23,98,4,0,28,49,8]
print(merge_sort(unsorted_array))

# test.TestCase.assertEqual((1 + 2), 3)a