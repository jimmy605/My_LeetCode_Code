# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        lyst = []
        
        curr_node = head 
        while curr_node:
            lyst.append(curr_node.val)
            
            if curr_node.next:
                curr_node = curr_node.next 
            else:
                break 
        
        return lyst[len(lyst) // 2]