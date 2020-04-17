"""
Just need to keep track of nodes that we have already seen along the way to Node A

        5                           5 then 3 then 20 then 21 then 10 then 1
     /     \
   3        10
  /  \     /
20   21   1


pre-order traversal looks like

if current != None
current
go left
go right


"""

def pre_order_traversal(node, max_val, count):
    if node != None:
        if node.value > max_val:
            print(node.value)
            count += 1
        count = max(pre_order_traversal(node.left, max(node.value, max_val), count), count)
        count = max(pre_order_traversal(node.right, max(node.value, max_val), count), count)
    return count

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree:
    def __init__(self):
        self.root = None

def visible_nodes():
    pass

if __name__ == "__main__":
    
    """
    Create Binary Search Tree First
    Oops, this is just a binary tree

    Hmmm how do you go about just creating a plain old binary tree?
    """

    tree = Tree()
    tree.root = TreeNode(5)

    node_left = TreeNode(3)
    node_left.left = TreeNode(20)
    node_left.right = TreeNode(21)

    node_right = TreeNode(10)
    node_right.left = TreeNode(1)

    tree.root.left = node_left
    tree.root.right = node_right
    
    # tree.root = TreeNode(-10)
    # node_right = TreeNode(-15)
    # node_right.right = TreeNode(-1)

    # tree.root.right = node_right

    count = pre_order_traversal(tree.root, -float('inf'), 0)