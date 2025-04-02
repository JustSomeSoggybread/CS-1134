def findChange (lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == 1 and lst[mid - 1] != 0:
            right = mid - 1
        
        elif lst[mid] == 0:
            left = mid + 1
        
        else:
            return mid