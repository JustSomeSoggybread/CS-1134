def find_duplicates(lst):
    hitList = [0] * len(lst)
    retListSize = 0
    retListIndex = 0
    for i in range(len(lst)):
        hitList[lst[i]] = hitList[lst[i]] + 1

    
    for i in range(len(hitList)):
        if (hitList[i] > 1):
            retListSize+=1
    retList = [0] * retListSize

    for i in range(len(hitList)):
        if (hitList[i] > 1):
            retList[retListIndex] = i
            retListIndex += 1

    return retList
