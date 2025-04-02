def count_lowercase(s, low, high):
    if len(s) == 0:
        return s
    total = 0
    if (s[low].islower() == True):
        total+=1
    if (high>low):
        prev = count_lowercase(s, low + 1, high)
        total+= prev
    return total

def is_number_of_lowercase_even(s, low, high):
    if (high>low):
        prev = (is_number_of_lowercase_even(s, low + 1, high))
        if (s[low].islower() == True):
            prev = not prev
        return prev
    else:
        return not s[low].islower()
