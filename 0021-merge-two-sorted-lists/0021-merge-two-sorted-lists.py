# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.head=ListNode(None)
        current3=self.head
        current1=list1
        current2=list2
        head_val=True
        new_head=None
        while current1 and current2:
            
              if current1.val<current2.val:
                 current3.next=current1
                 current3=current3.next
                 current1=current1.next
                 if head_val:
                    new_head=current3
                 head_val=False
                     
                 
              else:
                   current3.next=current2
                   current3=current3.next
                   current2=current2.next
                   if head_val:
                      new_head=current3
                   head_val=False
                       
        if current2:
            while current2:
                  current3.next=current2
                  current3=current3.next
                  current2=current2.next
                  if head_val:
                      new_head=current3
                  head_val=False
                       
        else:
              while current1:
                    current3.next=current1
                    current3=current3.next
                    current1=current1.next
                    if head_val:
                       new_head=current3
                    head_val=False
                       
        return new_head
                    
                   
                   
                 
                  