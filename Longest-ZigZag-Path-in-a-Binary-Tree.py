1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestZigZag(self, root: Optional[TreeNode]) -> int:
9        self.path = 0
10
11        def dfs(node, left, pathlen):
12            if node is None:
13                return
14            self.path = max(self.path, pathlen)
15            if left:
16                dfs(node.left, True, 1)
17                dfs(node.right, False, pathlen + 1)
18            else:
19                dfs(node.left, True, pathlen + 1)
20                dfs(node.right, False, 1)
21        dfs(root.right, False, 1)
22        dfs(root.left, True, 1)
23        return self.path