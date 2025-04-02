def sumSquares(n):
    total = 0
    for i in range(n):
        total+= i*i

    return total

def smallSquares(n):
    return sum(iter(i*i for i in range(n)), 0)

def oddSquares(n):
    total = 0
    for i in range(n):
        if i%2 == 1:
            total+= i*i
    return total

def smOddSquares(n):
    return sum(iter((2*i+1)*(2*i+1) for i in range(int (n/2))), 0)

def main():

    func1Result = sumSquares(7)
    func2Result = smallSquares(7)
    func3Result = oddSquares(7)
    func4Result = smOddSquares(7)

main()
