# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(float("-inf"))
        dummy.next=head
        left=head
        right=head.next
        def remove(node):
            node.next=node.next.next
        def  add(new_head,inserted):
             inserted.next=new_head.next
             new_head.next=inserted
             
            
        while right:
              if left.val<=right.val:
                  left=left.next
                  right=right.next
                  continue
              remove(left)
              current=dummy
              while  current and  current.next.val<=right.val:
                    current=current.next
              add(current,right)
              right=left.next
        return dummy.next
            
                    
        
       