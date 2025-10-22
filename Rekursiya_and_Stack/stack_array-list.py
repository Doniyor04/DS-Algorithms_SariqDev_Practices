array = [None] * 5

def len_arr(arr):
    # Listni uzunligini aniqlaydi
    i = 0
    for n in arr:
        if n != None:
            i += 1
    return i

def push(n, arr):
    # Listga element qo'shadi
    for num in arr:
        if num == None:
            arr[arr.index(num)] = n
            return
    print("Ro'yxat to'la")

def pop(arr):
    # Listni oxirgi elementini sug'urib oladi
    if not arr[0]: # To'plam bo'shligini tekshiradi
        return "To'plam bo'sh"
    
    if arr[-1] != None:
        num = arr[-1]
        arr[-1] = None
        return num
    
    for n in arr:
        if n == None:
            index_num = arr.index(n)
            num = arr[index_num-1]
            arr[index_num-1] = None
            return num
    
def isEmpty(arr):
    # Listni bo'shligini yoki nechta joy borligini tekshiradi
    if not arr[0]:
        return "To'plam bo'sh"
    
    arr_len = len(arr) - len_arr(arr)
    
    return f"To'plamda {arr_len} ta bo'sh joy bor" if arr_len > 0 else "To'plam to'la"

def isFull(arr):
    # Listni to'laligini yoki nechta element borligini tekshiradi
    if len_arr(arr) == len(arr):
        return "To'plam to'la"
    
    return f"To'plamda {len_arr(arr)} ta element bor" if len_arr(arr) > 0 else "To'plam bo'sh"

def peek(arr):
    # Listni oxirgi elementini ko'rsaradi
    if arr[0] == None: # List bo'shligini tekshiradi
        return "To'plam bo'sh"
    
    if arr[len(arr)-1] != None:
        num = arr[len(arr)-1]
        return num
    
    for n in arr:
        if n == None:
            index_num = arr.index(n)
            num = arr[index_num-1]
            return num

