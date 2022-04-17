# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        # prev, curr = None, head 
        
        # while curr:
        #     if curr.val == val:
        #         if prev:
        #             prev.next = curr.next
        #         else:
        #             head = curr.next 
        #         curr = curr.next
        #     else:
        #         prev, curr = curr, curr.next 
        
        # return head 
        
        dummy_head = ListNode(-1, head)
        
        current_node = dummy_head
        
        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next 
        
        return dummy_head.next 