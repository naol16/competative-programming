
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        met=False
        if not head  :
           return None
        while fast and fast.next:
              slow=slow.next
              fast=fast.next.next
              if slow==fast:
                 met=True
                 break
        if not met:
           return None
              
   
        slow=head
        while slow!=fast:
              slow=slow.next
              fast=fast.next
   
        return slow
