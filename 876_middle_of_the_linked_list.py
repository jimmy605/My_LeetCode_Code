# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        dummy_head = head 
        count = 0
        
        while dummy_head:
            dummy_head = dummy_head.next
            count += 1
        
        start_ind = count // 2
        ind = 0
        curr = head 
        while ind < start_ind:
            ind += 1
            curr = curr.next
        
        return curr  