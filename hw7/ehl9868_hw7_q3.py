
def is_height_balanced(bin_tree):
    def height_balanced_helper(root, is_equal):
        left_height = 0
        right_height = 0
        right_bal = True
        left_bal = True
        max_height = 0
        if (root.left is None and root.right is None):
            return (1, True)
        else:
            if (root.left is not None):
                left_height = height_balanced_helper(root.left, True)[0]
                left_bal = height_balanced_helper(root.left, True)[1]
                
            if (root.right is not None):
                right_height = height_balanced_helper(root.right, True)[0]
                right_bal = height_balanced_helper(root.right, True)[1]
        if (left_height >= right_height):
            max_height = left_height + 1
        else:
            max_height = right_height + 1

        if (abs(left_height - right_height)<=1 and left_bal and right_bal):
                return (max_height, True)
        else:
            return (max_height, False)
        
    if bin_tree.is_empty():
        raise Exception("Empty tree")

    return height_balanced_helper(bin_tree.root, True)[1]


