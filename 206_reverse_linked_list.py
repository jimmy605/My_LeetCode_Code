# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head 
        
        while curr:
            next_temp = curr.next 
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev

test = Solution()
test.reverseList([1,2,3,4,5])