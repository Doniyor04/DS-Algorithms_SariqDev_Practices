numbs = [58, 2, 91, 14, 73, 45, 33, 86, 60, 29]

def maxNum(l):
    if not l:
        return None
    
    maksimum = l[0]
    
    for n in l[1:]:
        if n > maksimum:
            maksimum = n
    return maksimum

def selection_sort(l):
    sort_list = []
    while l:
        max_num = maxNum(l)
        index_maxnum = l.index(max_num)
        sort_list.append(l.pop(index_maxnum))
    
    return sort_list
