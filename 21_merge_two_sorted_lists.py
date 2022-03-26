# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        list3 = []
        head1 = list1.head 
        head2 = list2.head 
        
        while True:
            
            while head1 <= head2:
                list3.append(head1)
                if not head1.next:
                    head1 = head1.next 
                else:
                    break 
            
            while head2 <= head1:
                list3.append(head2)
                if not head2.next:
                    head2 = head2.next 
                else:
                    break 
            
            if head1 == None and head2 == None:
                break
        
        return list3


