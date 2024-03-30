class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        total_sum=sum(shifts)%26
        newstring=""
        for j,i in enumerate(s):
            differnce=ord(i)-ord('a')
            new_letter=chr(ord('a')+(differnce+total_sum)%26)
            newstring+=new_letter
            total_sum=(total_sum-shifts[j])%26
        return newstring
            
      
                 
            
            
        