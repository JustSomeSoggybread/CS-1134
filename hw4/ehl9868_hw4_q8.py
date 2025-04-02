def flat_list(nested_lst, low, high):
    if len(nested_lst) == 0:
        return nested_lst
        
    if (low < high):
        if (isinstance(nested_lst[low], list)):
            return flat_list(nested_lst[low], 0, len(nested_lst[low])-1) + flat_list(nested_lst, low+1, high)
        else:
            return [nested_lst[low]] + flat_list(nested_lst, low+1, high)
    else:
        if (isinstance(nested_lst[low], list)):
            return flat_list(nested_lst[low], 0, len(nested_lst[low])-1)
        else: 
            return [nested_lst[low]]

lst = []
flat_list(lst, 0, 0)
print(lst)