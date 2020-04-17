"""
Given an inorder and preorder traversal reconstruct the binary tree



inorder
left (all the way down)
root
right (all the way down)

preorder
root
left (all the way down)
right (all the way down)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Steps:
1. Look at preorder first (tells us the root)
2. Look at preorder again (tells us all the left nodes)
3. Look at inorder (check if the first node is == preorder left)
    -> if yes then we know that's the match for the left handside of the tree
    -> if no, then we'll need to keep constructing the left hand side of the tree
yes
4. Tree left handside complete, look at preorder to begin constructing the right hand side of the tree




"""

        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root