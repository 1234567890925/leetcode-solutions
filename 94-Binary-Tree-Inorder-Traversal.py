#----------------------------------
'''
recursion -
time complexity = o(n) -> we check for each node
space complexity = O(n)

iteration -
time complexity = o(n) -> stack and another list - o(n)
space complexity = O(n)
'''
#----------------------------------

# inorder traversal: left -> main node -> right
#---------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # recursive - nested function - o(n)
        '''res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res'''

        # iterative - stack and another list - o(n)
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res