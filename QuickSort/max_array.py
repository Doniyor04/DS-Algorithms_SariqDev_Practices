def max_arr(arr: list):
    # To'xtash nuqtasi va list bo'shligini tekshiradi
    if not arr:
        return
    elif len(arr) == 1:
        return arr.pop()
    
    if arr[0] > arr[1]:
        arr.pop(1)
        return max_arr(arr)
    else:
        arr.pop(0)
        return max_arr(arr)
