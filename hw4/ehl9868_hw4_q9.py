def permutations(lst, low, high):
    if len(lst) == 0:
        return lst
    retList = []
    if low<high:
        
        sub = permutations(lst, low, high-1)

        for subperm in sub:
            for i in range(len(subperm)+1):
                retList.append(subperm[:i] + [lst[high]] + subperm[i:])
                print(i)
            
    else:
        retList.append([lst[high]])


    return retList

lst= [1,2,3]
print(permutations(lst, 0, 2))