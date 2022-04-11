# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        is_pal_list = []
        node = head
        
        while node:
            is_pal_list.append(node.val)
            
            if node.next:
                node = node.next 
            else:
                break 
        
        return is_pal_list == is_pal_list[::-1]

test = Solution()
test.isPalindrome([head])