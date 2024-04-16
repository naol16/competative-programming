# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def reverseBetween(self, head, left, right):
#         """
#         :type head: ListNode
#         :type left: int
#         :type right: int
#         :rtype: ListNode
#         """
#         current=head
#         first_head=head
#         left_index=left
#         number=1
            
#         while current and number<left:
#               if number==left-1:
#                  new_left=current
#               current=current.next
#               number+=1
#         left_node=current
#         right_index=right
#         while current  and number<right_index:
#               current=current.next
#               number+=1
        
               
#         right_node=current
#         number=0
#         current=left_node
#         prev=new_left
#         new2=new_left.next
#         while  current  and number+left-1<right_index:
#                 next=current.next
#                 current.next=prev
#                 prev=current
#                 current=next
#         new_left.next=prev
#         new2.next=right_node.next 
#         print(left_node.val)
#         print(right_node.val)
#         print(new_left.next.val)
#         return head
class Solution(object):
    def reverseBetween(self, head, left, right):
        current = head
        prev = None
        number = 1
        new_left=None
            
        while current and number < left:
            if number == left - 1:
                new_left = current
            current = current.next
            number += 1
        left_node = current
        
        right_index = right
        while current and number < right_index:
            current = current.next
            number += 1
        right_node = current
        
        number = 0
        current = left_node
        while current and number < right - left + 1:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            number += 1
        
        if new_left:
            new_left.next = prev
        else:
            head = prev
        left_node.next = current
        
        return head

        
        
         
               
                
            
            