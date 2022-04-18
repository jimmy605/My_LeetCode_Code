# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_str = ''
        
        curr = head 
        if curr.next == None:
            bin_str += str(curr.val)
        else:
            while curr:
                bin_str += str(curr.val)
                curr = curr.next 
        
        return int(bin_str, base=2)