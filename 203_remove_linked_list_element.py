# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        curr_node = head 
        pre_node = ListNode(0) 
        
        while curr_node:
            if curr_node.val == val:
                pre_node.next = curr_node.next 
            else:
                pre_node = curr_node
            curr_node = curr_node.next 
        
        return pre_node