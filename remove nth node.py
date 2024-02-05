# # Definition for singly-linked list.
# classListNode(object):
#     def __init__(self, val=0, next=None):
#           self.val = val
#           self.next = next
class Solution(object):
    
        
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current=head
        leng=0
        while current:
              current=current.next
              leng+=1
        index=leng-n
        prev=head
        i=1
        if n==leng:
           return head.next
        while i<index:
              prev=prev.next
              i+=1
        
        prev.next=prev.next.next
        return head
