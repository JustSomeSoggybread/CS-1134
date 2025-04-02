from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue

def permutations(lst):
    s = ArrayStack()
    q = ArrayQueue()

    for elem in lst:
        s.push(elem)
    
    q.enqueue([])
    while not s.is_empty():
        top = s.pop()
        for i in range(len(q)):
            p = q.dequeue()
            for n in range(len(p) + 1):
                q.enqueue(p[:n] + [top] + p[n:])
    retList = []

    while not q.is_empty():
        retList.append(q.dequeue())

    return retList