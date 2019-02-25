# next biggest number
def find_next(n):
    n = list(str(n))
    for i in range(len(n)-1, 0, -1):
        if n[i] > n[i-1]:
            n = n[:i-1] + swap_number(n[i:], n[i-1])
            n = n[:i] + sorted(n[i:])
            return int(''.join(n))

    return -1

def swap_number(array, number):
    for i in range(len(array)-1, 0, -1):
        if array[i] > number:
            temp = array[i]
            array[i] = number
            array.insert(0, temp)
            return array

    array.append(number)
    return array

nbn = 829774
print(find_next(nbn))