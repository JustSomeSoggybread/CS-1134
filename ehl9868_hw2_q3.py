def factors (num):
    numList = [0] * int(num**0.5)
    returnNum = 1
    factorCount = 0

    while returnNum**2 <= num:
        if (num%returnNum == 0):
            yield returnNum
            numList[factorCount] = int (num/returnNum)
            factorCount += 1
        returnNum+=1
    returnNum -= 1

    for i in range(factorCount):
        if (numList[factorCount - 1 - i] != returnNum):
            yield numList[factorCount - 1 - i]