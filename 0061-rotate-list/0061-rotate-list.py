# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next           
# class Solution(object):
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         current=head
#         num=1
#         prev=None
        
#         length=1
#         if not head:
#           return None
        
#         while current.next:
              
#               current=current.next
#               length+=1
#         k=k%length
#         if k==0:
#            return head
#         last_element=current
#         current=head
       
#         left=head
#         for  i in range(0,length-k-1):
#              left=left.next
              
#         right=left.next
#         left.next=None
#         last_element.next=head
#         return right
class Solution(object):
    def rotateRight(self, head, k):
        """"
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current=head
        num=1
        prev=None
        
        length=0
        if not head:
          return None
        
        while current:
              prev=current
              current=current.next
              length+=1
        k=k%length
        last_element=prev
        current=head
       
        left=head
        for  i in range(1,length-k):
             left=left.next
        if k==0:
           return head
        right=left.next
        left.next=None
        last_element.next=head
        return right
            
              
            
                            