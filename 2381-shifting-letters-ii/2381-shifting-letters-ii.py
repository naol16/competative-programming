class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        list1=list(s)
        row=len(shifts)
        new_string=""
        new_string2=""
        new_list=[0]*(len(s)+1)
        total_sum=0
                  
        for i in range(row):
            if shifts[i][2]==0:
               new_list[shifts[i][0]]+=-1
               new_list[shifts[i][1]+1]-=-1
                   
            elif shifts[i][2]==1:
                 new_list[shifts[i][0]]+=1
                 new_list[shifts[i][1]+1]-=1
                      
                     
        for i in range(len(s)):
            total_sum+=new_list[i]
            new_list[i]=total_sum
            
        for i,j in  enumerate(new_list):
            if i<=len(list1)-1:
               new_string+=chr((ord(s[i]) - ord('a')+new_list[i]) % 26 + ord('a'))
            
                                  
        
        return new_string
        
                