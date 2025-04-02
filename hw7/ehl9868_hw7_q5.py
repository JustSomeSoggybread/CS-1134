from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    exp_list = prefix_exp_str.split()
    operators = "+-*/"
    def create_expression_tree_helper(prefix_exp, start_pos):
        if (start_pos >= len(prefix_exp)):
            return None, 0
       
        elif prefix_exp[start_pos] in operators:
            root = LinkedBinaryTree.Node(prefix_exp[start_pos])
            left_tree = create_expression_tree_helper(prefix_exp, start_pos+1)[0]
            left_size = create_expression_tree_helper(prefix_exp, start_pos+1)[1]

            right_tree = create_expression_tree_helper(prefix_exp, start_pos+left_size+1)[0]
            right_size = create_expression_tree_helper(prefix_exp, start_pos+left_size+1)[1]

            root.left = left_tree
            root.right = right_tree

            return (root, left_size + right_size + 1)
        
        else:
            root = LinkedBinaryTree.Node(int(prefix_exp[start_pos]))
            return root, 1
    
    retTree = LinkedBinaryTree()
    retTree.root = create_expression_tree_helper(exp_list, 0)[0]
    return retTree

def prefix_to_postfix(prefix_exp_str):
    exp_tree = create_expression_tree(prefix_exp_str)
    nList = list(exp_tree.postorder())
    return " ".join([str(item.data) for item in nList])