
def two_sum(srt_lst, target):
    leftPointer = 0
    rightPointer = len(srt_lst) - 1

    for i in range(len(srt_lst)):
        if (srt_lst[leftPointer] + srt_lst[rightPointer] == target):
            return (leftPointer, rightPointer)
        elif (srt_lst[leftPointer] + srt_lst[rightPointer] > target):
            rightPointer -= 1
        elif (srt_lst[leftPointer] + srt_lst[rightPointer] < target):
            leftPointer += 1
    return None