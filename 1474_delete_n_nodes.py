# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        initial_offset = 1
        
        while head:
            
            for i in range(m - initial_offset):
                if head is None:
                    break 
                head = head.next 
            
            for j in range(n):
                if head is None or head.next is None:
                    break 
                head.next = head.next.next 
            
            initial_offset = 0 
        
        return dummy.next