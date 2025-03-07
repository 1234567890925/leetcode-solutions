#----------------------------------
'''
recursion dfs -
time complexity = o(n) 
space complexity = O(h) -> height of the tree

iteration dfs -
time complexity = o(n) 
space complexity = O(h) -> height of the tree

iteration bfs -
time complexity = o(n)
space complexity = O(w) -> max width of the tree
'''
#----------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive dfs
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
'''

#iterative dfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth +1])
                stack.append([node.right, depth+1])
        return res


#iterative bfs
    #traverse level by level
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
'''