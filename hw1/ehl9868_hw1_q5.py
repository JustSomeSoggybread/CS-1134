def fibs(n):
    for i in range(n):
        
        if i < 2 :
            yield 1
            oneback = 1
            twoback = 1
        else:
            returnThis = oneback+twoback
            yield (returnThis)
            twoback = oneback
            oneback = returnThis

for cur in fibs(8):
    print(cur)
