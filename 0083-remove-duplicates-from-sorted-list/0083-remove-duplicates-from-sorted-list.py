# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
           return None
        elif head and not head.next:
             return head
        prev=head
        current=head.next
       
        while current:
              while current and  current.val==prev.val:
                    prev.next=current.next
                    current=current.next
              if current:
                 prev=prev.next
                 current=current.next
        return head
              
        