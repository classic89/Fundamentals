'''
Authors: JT, Noe
Run time: O(N)

Problem: (https://www.codewars.com/kata/consecutive-strings)
You are given an array strarr of strings and an integer k.
Your task is to return the first longest string consisting of
k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption

'''

def longest_consec(strarr, k):
    if not len(strarr) or k <= 0 or k > len(strarr):
        return ""
      
    initial_combined_length = 0
    start_max_index = 0
    
    for i in range(0, k):
        initial_combined_length += len(strarr[i])
        
    jt_string_length = initial_combined_length
    
    for i in range(k, len(strarr)):
        jt_string_length += len(strarr[i]) - len(strarr[i-k])
        if jt_string_length > initial_combined_length:
            initial_combined_length = jt_string_length
            start_max_index = i-k+1
    
    combined_string = ""
    for i in range(start_max_index, start_max_index+k):
        combined_string += strarr[i]
        
    return combined_string

result = longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)
print(result)