class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        new=""
        for i in address:
            if i==".":
               new+="[.]"
            else:
                 new+=i
        return new
        
