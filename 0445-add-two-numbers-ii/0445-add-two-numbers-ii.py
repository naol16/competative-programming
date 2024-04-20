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
               
        prev = None
        dummy1 = ListNode(None)
        dummy1.next = l1
        current1 = dummy1.next
        k = 0
        
        while current1:
            next_node = current1.next
            current1.next = prev
            prev = current1
            current1 = next_node
        current1 = prev
        
        prev = None
        dummy2 = ListNode(None)
        dummy2.next = l2
        current2 = dummy2.next
        
        while current2:
            next_node = current2.next
            current2.next = prev
            prev = current2
            current2 = next_node
        current2 = prev 
        
        new_head = ListNode()
        current = new_head
        
        while current1 and current2:
            node_val = current1.val + current2.val + k
            k = node_val // 10
            node_val = node_val % 10
            new_node = ListNode(node_val)
            current.next = new_node
            current = current.next
            current1 = current1.next
            current2 = current2.next
        
        if current2:
            while current2:
                node_val = current2.val + k
                k = node_val // 10
                node_val = node_val % 10
                new_node = ListNode(node_val)
                current.next = new_node
                current = current.next
                current2 = current2.next
        elif current1:
            while current1:
                node_val = current1.val + k
                k = node_val // 10
                node_val = node_val % 10
                new_node = ListNode(node_val)
                current.next = new_node
                current = current.next
                current1 = current1.next 
        
        if k:
            new_node = ListNode(k)
            current.next = new_node
        
        prev = None
        current3 = new_head.next
        
        while current3:
            next_node = current3.next
            current3.next = prev
            prev = current3
            current3 = next_node
        
        return prev       
        prev = None
        dummy1 = ListNode(None)
        dummy1.next = l1
        current1 = dummy1.next
        k = 0
        
        while current1:
            next_node = current1.next
            current1.next = prev
            prev = current1
            current1 = next_node
        current1 = prev
        
        prev = None
        dummy2 = ListNode(None)
        dummy2.next = l2
        current2 = dummy2.next
        
        while current2:
            next_node = current2.next
            current2.next = prev
            prev = current2
            current2 = next_node
        current2 = prev 
        
        new_head = ListNode()
        current = new_head
        
        while current1 and current2:
            node_val = current1.val + current2.val + k
            k = node_val // 10
            node_val = node_val % 10
            new_node = ListNode(node_val)
            current.next = new_node
            current = current.next
            current1 = current1.next
            current2 = current2.next
        
        if current2:
            while current2:
                node_val = current2.val + k
                k = node_val // 10
                node_val = node_val % 10
                new_node = ListNode(node_val)
                current.next = new_node
                current = current.next
                current2 = current2.next
        elif current1:
            while current1:
                node_val = current1.val + k
                k = node_val // 10
                node_val = node_val % 10
                new_node = ListNode(node_val)
                current.next = new_node
                current = current.next
                current1 = current1.next 
        
        if k:
            new_node = ListNode(k)
            current.next = new_node
        
        prev = None
        current3 = new_head.next
        
        while current3:
            next_node = current3.next
            current3.next = prev
            prev = current3
            current3 = next_node
        
        return prev
               
        
        
         
        
        