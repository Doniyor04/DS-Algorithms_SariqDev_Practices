myList = [1,3,4,6,5,8,10,61,55,45,56,201,91]
myList.sort()
son = 6

def binary_s(n, ls):
    l = 0
    h = len(ls) - 1

    while l <= h:
        m = (l+h)//2

        if ls[m] > n:
            h = m - 1
        elif ls[m] < n:
            l = m + 1
        else:
            return ls.index(n)

    return -1

print(binary_s(son, myList))