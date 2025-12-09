1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        if root is None:
10            return None
11        if root.val == val:
12            return root
13        if val<root.val:
14            return self.searchBST(root.left, val)
15        else:
16            return self.searchBST(root.right, val)
17