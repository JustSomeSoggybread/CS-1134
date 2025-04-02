import math

def main():
    ListA = [int (math.pow(10, i)) for i in range(6)]
    ListB = [i * (i+1) for i in range(10)]
    ListC = [chr(97 + i) for i in range(26)]

main()
