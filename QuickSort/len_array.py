def len_arr(arr: list):
    # To'xtash nuqtasi va array bo'sh yoki yo'qligini ham tekshiradi
    if not arr:
        return 0
    arr.pop()
    return len_arr(arr) + 1

