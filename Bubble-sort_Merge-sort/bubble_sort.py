# Iterativ
def bubble_sort_i(arr: list):

    if not arr:
        return False
    
    arr_c = arr[:]
    n = len(arr_c)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_c[j] > arr_c[j+1]:
                arr_c[j], arr_c[j+1] = arr_c[j+1], arr_c[j]
                 
    return arr_c


# Recursive

def bubble_sort_r(arr: list, n=None):

    if n is None:
        n = len(arr)
    
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return bubble_sort_r(arr, n-1)
