# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#생각을 해보자 일단 이거 하려면 p랑 q의 위치부터 찾아야 함. 그리고 p또는 q를 찾기 전에 먼저 해시맵에다가 그 value를 찾아서 넣는 느낌으로 짜보자


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        answer = None
        state = True
        def helper(root, p, q):
            count = 0
            if root is None:
                return 0
            if root == p or root == q:
                count = 1
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            lca = left + right + count
            nonlocal state
            if lca == 2 and state:
                nonlocal answer
                answer = root
                state = False
            return lca
        helper(root, p, q)
        return answer


            