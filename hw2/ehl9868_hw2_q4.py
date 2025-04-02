def e_approx(n):
    denominator = 1

    sum = 1
    for i in range(n):
        sum += 1/denominator
        denominator *= i+2
    return sum