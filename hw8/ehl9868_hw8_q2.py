from BinarySearchTreeMap import BinarySearchTreeMap

def create_chain_bst(n):
    returnTree = BinarySearchTreeMap()
    for elem in range(1, n+1):
        returnTree[elem] = None
    return returnTree

def create_complete_bst(n):

    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low == high:
        bst[low] = None
    elif low < high:
        mid = (low + high) // 2
        bst[mid] = None
        add_items(bst, low, mid-1)
        add_items(bst, mid+1, high)