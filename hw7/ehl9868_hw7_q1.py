from LinkedBinaryTree import LinkedBinaryTree

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        min = root.data
        max = root.data

        if (root.left is None and root.right is None):
            return (min, max)
        else:
            if (root.left is not None):
                if subtree_min_and_max(root.left)[0] < min:
                    min = subtree_min_and_max(root.left)[0]
                if subtree_min_and_max(root.left)[1] > max:
                    max = subtree_min_and_max(root.left)[1]
            if (root.right is not None):
                if subtree_min_and_max(root.right)[0] < min:
                    min = subtree_min_and_max(root.right)[0]
                if subtree_min_and_max(root.right)[1] > max:
                    max = subtree_min_and_max(root.right)[1]
            return (min, max)

    if bin_tree.root is None:
        raise Exception("Empty tree")
    return subtree_min_and_max(bin_tree.root)


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
bin_tree = LinkedBinaryTree(f)

print(min_and_max(bin_tree))