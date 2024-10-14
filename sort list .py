class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newarr= []
        current = head
        while current:
            newarr.append(current.val)
            current = current.next

        newarr.sort()
      
        dummy = ListNode(0)
        current = dummy
        
        for val in newarr:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
          
