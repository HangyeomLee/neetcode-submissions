# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        self.answer = 0                  # 지금까지 본 가장 큰 count (공유 변수)
        count = 1
        def helper(node, count):         # maxDepth 안에 만든 함수
            if node == None:
                return                   # 값 없이 그냥 돌아감
            self.answer = max(self.answer, count)           # 최댓값 갱신
            helper(node.left, count + 1 )       # 왼쪽으로 내려가기
            helper(node.right, count + 1)       # 오른쪽으로 내려가기

        helper(root, count)           # 시작점
        return self.answer