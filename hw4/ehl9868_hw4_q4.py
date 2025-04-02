def list_min(lst, low, high):
    if len(lst) == 0:
        return lst
    if (high-low) == 0:
        return lst[low]
    prev = list_min(lst, low + 1, high)
    if prev < lst[low]:
        return prev
    return lst[low]