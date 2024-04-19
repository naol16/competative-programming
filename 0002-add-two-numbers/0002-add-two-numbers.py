# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1=l1
        node2=l2
        node_val=node1.val+node2.val
        # node4=ListNode(node_val,None)
        newhead=ListNode()
        current=newhead
        k=0
        while node1 and  node2:
              node_val=node1.val+node2.val+k
              if node_val>9:
                  value=node_val%10
                  new_node=ListNode(value,None)
                  k=node_val//10
                 
              else:
                   new_node=ListNode(node_val,None)
                   k=0
              current.next=new_node
              current=new_node
              node1=node1.next
              node2=node2.next
        if node2:
           while node2:
                 node_val=node2.val+k
                 if node_val>9:
                    value=node_val%10
                    new_node=ListNode(value,None)
                    k=node_val//10
                 
                 else:
                     new_node=ListNode(node_val,None)
                     k=0
                 current.next=new_node
                 current=new_node
                 node2=node2.next
        elif node1:
             while node1:
                   node_val=node1.val+k
                   if node_val>9:
                      value=node_val%10
                      new_node=ListNode(value,None)
                      k=node_val//10
                 
                   else:
                        new_node=ListNode(node_val,None)
                        k=0
                   current.next=new_node
                   current=new_node
                   node1=node1.next 
        if k:
           node_val=k
           new_node=ListNode(k,None)
           current.next=new_node
              
        return newhead.next
            
        
        
        
        
        