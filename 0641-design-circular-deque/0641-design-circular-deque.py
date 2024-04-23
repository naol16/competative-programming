from collections import deque
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k=k
        self.qeue=[]

        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.k==len(self.qeue):
           return False
    
        self.qeue.insert(0,value)
        return True
        


        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.qeue)==self.k:
           return False
        
        self.qeue.append(value)
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.qeue:
           self.qeue.pop(0)
           return True
        return False
    
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.qeue:
           self.qeue.pop()
           return True
        
        return False
        

    def getFront(self):
        """
        :rtype: int
        """
        if self.qeue:
           return self.qeue[0]
        else:
             return -1
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.qeue:
           
           return self.qeue[-1]
        else:
             return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.qeue:
           return False
        else:
             return True
        
        

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.qeue)==self.k:
           return True
        else:
             return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()