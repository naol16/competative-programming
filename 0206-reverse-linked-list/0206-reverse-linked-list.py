# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        prev=None
        while current:
             
             
             next=current.next
             current.next=prev
             prev=current
             current=next
        self.head=prev
        
        return self.head