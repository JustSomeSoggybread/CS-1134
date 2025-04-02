def appearances(s, low, high):
    if len(s) == 0:
        return s
    if (low < high):
        dict = appearances(s, low, high-1)
    else:
        dict = {}

    if s[high] in dict.keys():
        value = dict[s[high]]
        dict.update({s[high] : value + 1})
    else:
        dict.update({s[high]: 1})

    return dict
