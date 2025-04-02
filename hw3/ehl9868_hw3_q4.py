def remove_all(lst, value):
    swapPointer = 0
    normPointer = 0
    cut = 0

    while (swapPointer < len(lst)):
        if (lst[swapPointer] == value):
            swapPointer += 1
            cut += 1
        else:
            lst[normPointer] = lst[swapPointer]
            swapPointer += 1
            normPointer += 1
    for i in range(cut):
        lst.pop()
    return lst