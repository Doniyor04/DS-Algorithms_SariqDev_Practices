def sum(arr):
    # List bo'sh bo'lsa 0 qaytaradi
    if not arr:
        return 0
    # Listda 1 ta element bo'lsa usha elementni qaytaradi
    if len(arr) == 1:
        return arr[0]
    
    # Listdagi birinchi elementni pop() bilan oladi va funksiyaga qo'shadi
    return arr.pop(0) + sum(arr)