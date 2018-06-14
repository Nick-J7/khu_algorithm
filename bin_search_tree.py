#import utility

class Node:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data


def bin_search_tree_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left_child is None:
                root.left_child = node
            else:
                bin_search_tree_insert(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
            else:
                bin_search_tree_insert(root.right_child, node)


def max_value_node(root):
    while root.right_child is None:
        return root


def bin_search_tree_delete(root, data):
    if root is None:
        return None

    if root.data == data:
        if root.left_child is None and root.right_child is not None:
            root = root.right_child
            return root
        elif root.right_child is None and root.left_child is not None:
            root = root.left_child
            return root
        elif root.left_child is None and root.right_child is None:
            return None
        else:
            temp = root
            root = max_value_node(root.left_child)
            root.left_child = temp
            print("Exception")

    elif root.data < data:
        root.right_child = bin_search_tree_delete(root.right_child, data)
    else:
        root.left_child = bin_search_tree_delete(root.left_child, data)

    return root



def print_inOrder(root):
    if root is not None:
        print_inOrder(root.left_child)
        print(root.data)
        print_inOrder(root.right_child)


def print_preOrder(root):
    if root is not None:
        print(root.data)
        print_inOrder(root.left_child)
        print_inOrder(root.right_child)


r = Node(7)
bin_search_tree_insert(r, Node(9))
bin_search_tree_insert(r, Node(1))
bin_search_tree_insert(r, Node(3))
bin_search_tree_insert(r, Node(12))

print_inOrder(r)
print()
#print_preOrder(r)

r = bin_search_tree_delete(r, 12)
print_inOrder(r)
