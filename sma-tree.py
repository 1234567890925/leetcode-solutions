from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
#----------------------MAIN CODE----------------------------
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
#----------------------MAIN CODE----------------------------


def list_to_tree(lst):
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while i < len(lst):
        current = queue.pop(0)
        
        if i < len(lst) and lst[i] is not None:  # Left child
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:  # Right child
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    
    return root

sol = Solution()
p = list_to_tree([1,2,3])  # Convert the list to a TreeNode
q = list_to_tree([1,2,3])  # Convert the list to a TreeNode
res = sol.isSameTree(p, q)
print(res)