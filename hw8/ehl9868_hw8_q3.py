from BinarySearchTreeMap import BinarySearchTreeMap

def restore_bst(prefix_lst):
    def restore_helper(prefix_lst, low, high):
        
        if low > high:
            return None

        else:

            root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[low]))
            
            leftIndex = low + 1
            while leftIndex <= high and prefix_lst[leftIndex] < root.item.key:
                leftIndex+=1
            
            root.left = restore_helper(prefix_lst, low + 1, leftIndex - 1)
            root.right = restore_helper(prefix_lst, leftIndex, high)

            return root
    
    retTree = BinarySearchTreeMap()
    retTree.root = restore_helper(prefix_lst, 0, len(prefix_lst) - 1)

    return retTree

