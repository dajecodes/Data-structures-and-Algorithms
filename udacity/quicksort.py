"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array)<=1:
        return array 
    else:
        p=array.pop()
        left_array=[]
        right_array=[]
        for e in array:
            if e<p:
                left_array.append(e)
            else:
                right_array.append(e)

    return quicksort(left_array)+[p]+quicksort(right_array)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))