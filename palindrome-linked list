
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        string1=''
        string2=''
        prev=None
        current=head
        while current:
              string1+=str(current.val)
              current=current.next



        if string1==string1[::-1]:
           return True
        else:
         return False
