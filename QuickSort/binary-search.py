# Namuna
myList = [1,3,4,6,5,8,10,61,55,45,56,201,91]
myList.sort()
son = 8
l = 0
h = len(myList) - 1

def binary_search(arr: list, num: int, min: int, max: int):
    # Listni bo'shligini tekshiradi
    if not arr:
        return
    
    # Son ro'yxatni ichida yo'q bo'lsa
    if min > max:
        return -1
    
    m = (min + max)//2
    
    # To'xtash nuqtasi
    if arr[m] == num:
        return arr.index(num)
    
    b_s = binary_search(arr, num, min, m-1) if arr[m] > num else binary_search(arr, num, m+1, max)

    return b_s

binary_search(myList, son, l, h)