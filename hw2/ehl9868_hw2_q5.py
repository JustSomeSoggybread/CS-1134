def split_parity(lst):
    evenPointer = len(lst) -1
    oddPointer = 0

    while evenPointer > oddPointer:
        while lst[evenPointer] % 2 == 0 and evenPointer > oddPointer:
            evenPointer -= 1
        while lst[oddPointer] % 2 == 1 and oddPointer < evenPointer:
            oddPointer += 1
        lst[evenPointer], lst[oddPointer] = lst[oddPointer], lst[evenPointer]

    return lst