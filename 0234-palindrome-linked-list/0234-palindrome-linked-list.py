# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        prev=None
        current=head
        num1=""
        num2=""
        while current:
               num1+=str(current.val)
               current=current.next
        current=head
        while current:
              next=current.next
              current.next=prev
              prev=current
              current=next
        current=prev
        while  current:
               num2+=str(current.val)
               current=current.next
    
        if num1==num2:
           return True
        
    
        else:
             return False
        
              
               
              
              
        