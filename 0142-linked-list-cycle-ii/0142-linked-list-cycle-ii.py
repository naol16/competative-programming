# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast=head
        slow=head
        detect=False
        while fast and fast.next:
              fast=fast.next.next
              slow=slow.next
              if slow==fast:
                 detect=True
                 break
        slow=head
        while fast and  slow!=fast:
              slow=slow.next
              fast=fast.next
        if detect:
           return slow
            
                        
        return None