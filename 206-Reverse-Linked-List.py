#----------------------------------
'''
iterative -
time complexity = o(n)
space complexity = O(1)

recursive -
time complexity = o(n) -> The recursion continues until it reaches the end of the list
space complexity = O(n)  -> Each recursive call adds a new frame to the call stack
'''
#----------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        ITERATIVE:
        --------------
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev'''

        #RECURSIVE:
        def reverse(curr, prev = None):
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            return reverse(nxt, curr)
        return reverse(head)