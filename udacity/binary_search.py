"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    mid_index=None
    mid_elemnt=None
    left_array=None
    right_array=None
    if len(input_array)==1:
        if input_array[0]== value:            
            return 0
    elif len(input_array)==2:
        if input_array[0]==value:
            return 0
        elif input_array[1]==value:
            return 1
    else:
        mid_index=int(len(input_array)/2)
        mid_elemnt=input_array[mid_index]
        left_array=input_array[:mid_index]
        right_array=input_array[mid_index+1 :]       
        if mid_elemnt==value:
            return(mid_index)
        elif mid_elemnt>value:
            i=(binary_search(left_array,value))
            if i==-1:
                return -1
            else:
                return(mid_index-(len(left_array)-i))
        else:
            i=(binary_search(right_array,value))
            if i==-1:
                return -1
            else:
                return(mid_index+i+1)


    return -1


# test_list = [1,3,9,11,15,19,29]
test_list = [1,3,9,11,15,19,29,32,35,36,40,41,47,52,55,57,59,62,63,66,68]
test_val1 = 41

test_val2 = 15
print (binary_search(test_list, test_val1))
# print (binary_search(test_list, test_val2))