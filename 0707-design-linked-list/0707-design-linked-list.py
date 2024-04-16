class Node:
      def __init__(self,val):
          self.val=val
          self.next=None   


class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        current=self.head
        number=0
        while number<index  and  self.size>index:
              current=current.next
              number+=1
        return  current.val
               
        
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.size+=1
        
        
        

        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode=Node(val)
        current=self.head
        if not self.head: # if self.size == 0:
            self.head = newnode
        else:
             current=self.head
             number=0
             while current.next:
                   current=current.next
                   number+=1
             newnode=Node(val)
             current.next=newnode
        self.size+=1
        
                
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
            
        elif index == self.size:
            self.addAtTail(val)
            
        elif 0 < index and index< self.size:
             newnode=Node(val)
             current=self.head
             number=0
             while  current.next and index-1>number:
                    current=current.next
                    number+=1
             newnode.next=current.next
             current.next=newnode
             self.size+=1
        else:
            return
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)