from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        counter=Counter(s)
        b=''
        a=sorted(counter.items(),key=lambda x:x[1],reverse=True)
        for char,freq in a:

            b+=char*freq
        return(b)
