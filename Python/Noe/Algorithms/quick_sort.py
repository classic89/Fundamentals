'''
TODO: Implement unit tests
Algorithm steps:
1. Pick a pivot and move it to the end of the array or just pick the end of the array as a pivot.
    selecting the median of three random values will increase the runtime efficiency
2. Partition the array, values less than the pivot go to the left of it, values greater go to the right
3. recursively partition the left and right side of each pivot until the array section being partitioned is of length 1
'''

def quick_sort(array, start, end):
    if start < end:
        partition_index = partition(array, start, end)
        quick_sort(array, start, partition_index-1)
        quick_sort(array, partition_index+1, end)


def partition(array, start, end):
    pivot = array[end]
    p_index = start
    for i in range(start, end):
        if array[i] <= pivot:
            tmp = array[i]
            array[i] = array[p_index]
            array[p_index] = tmp
            p_index += 1

    array[end] = array[p_index]
    array[p_index] = pivot

    return p_index


# input variables
unsorted_array = [5,3,7,34,7,23,98,4,0,28,49,8]
quick_sort(unsorted_array, 0, len(unsorted_array)-1)
print(unsorted_array)