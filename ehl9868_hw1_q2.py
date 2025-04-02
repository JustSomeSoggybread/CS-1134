def shift (lst, k, dir = 'left'):
    if dir == 'right':
        tempList = [lst[len(lst) - k + i] for i in range(k)]
        for i in range(len(lst)-k):
            lst[len(lst) - i - 1] = lst[len(lst) - i - k - 1]
        for i in range(k):
            lst[i] = tempList[i]

    if dir == 'left':
        tempList = [lst[i] for i in range(k)]
        for i in range(len(lst)-k):
            lst[i] = lst[i+k]
        for i in range(k):
            lst[len(lst) - k + i]  = tempList[i]
    return lst