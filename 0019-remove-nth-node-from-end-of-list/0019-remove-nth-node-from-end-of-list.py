# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current=head
        self.length=0
        num=1
        while current:
              current=current.next
              self.length+=1
        newnum=self.length-n
        current=head
        while current and num<newnum:
               current=current.next
               num+=1
        if n==self.length:
           return head.next
        
        current.next=current.next.next
        return head
        
        
        