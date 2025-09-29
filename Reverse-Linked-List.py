# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''   
        # 1st way-
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        #2nd way-
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p'''

        # 3rd way-
        def reverse(curr, prev=None):
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            return reverse(nxt, curr)
        return reverse(head)