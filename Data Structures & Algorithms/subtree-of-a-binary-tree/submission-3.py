# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRoot_copy = subRoot
        def searcher(node):
            subRoot = subRoot_copy
            if node == None:
                return False
            elif checker(node,subRoot) == True:
                return True
            else:
                return searcher(node.left) or searcher(node.right)


        def checker(node, subnode):
            if node == None and subnode == None:
                return True
            elif node == None or subnode == None:
                return False
            elif node.val == subnode.val:
                return checker(node.left,subnode.left) and checker(node.right,subnode.right)
            else:
                return False
        
        return searcher(root)