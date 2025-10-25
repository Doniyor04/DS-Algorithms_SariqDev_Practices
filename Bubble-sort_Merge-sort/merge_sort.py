array = [2, -1, 5, 4]

# n = len(array) // 2
# arr1 = array[:n]
# arr2 = array[n:]


def merge_sort(arr: list):
    if not arr:
        return
    n = len(arr) // 2
    if len(arr) != 1:
        arr1 = arr[:n]
        arr2 = arr[n:]
        l1 = merge_sort(arr1)
        l2 = merge_sort(arr2)
    else:
        return arr
    



merge_sort(array)
