class Solution(object):
    
     
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        met=False
        if fast and fast.next is None:
            return False
        else:
             while fast and fast.next:
                   slow=slow.next
                   fast=fast.next.next
                   if fast==slow:
                      return True
