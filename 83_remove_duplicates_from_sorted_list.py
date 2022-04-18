# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head == []:
            return head
        if head.next == None:
            return head
        
        curr = head 
        while curr.next:
            next_node_val = curr.next.val 
            if curr.val == next_node_val and curr.next.next:
                curr.next = curr.next.next
            elif curr.val == next_node_val:
                curr.next = None 
            else:
                curr = curr.next 
            
        return head 