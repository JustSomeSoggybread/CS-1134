from BinarySearchTreeMap import BinarySearchTreeMap

def find_min_abs_difference(bst):
    def find_min_abs_difference_helper(root):
        if root == None:
            return float('inf'), 0, float('inf')

        else:
            leftmin, leftmax, leftmad = find_min_abs_difference_helper(root.left)
            print("LMin: ", leftmin, "LMax: ", leftmax, "LMad: ", leftmad)
            rightmin, rightmax, rightmad = find_min_abs_difference_helper(root.right)
            print("RMin: ", rightmin, "RMax: ", rightmax, "RMad: ", rightmad)

            retmad = min(leftmad, rightmad, abs(root.item.key - leftmax), abs(rightmin - root.item.key))
            retmin = min(leftmin, rightmin, root.item.key)
            retmax = max(leftmax, rightmax, root.item.key)

            return retmin, retmax, retmad
    
    return find_min_abs_difference_helper(bst.root)[2]

