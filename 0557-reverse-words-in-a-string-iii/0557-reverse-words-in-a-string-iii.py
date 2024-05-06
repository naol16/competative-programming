class Solution:
    def reverseWords(self, s: str) -> str:
        newlist=" "
        list1=s.split(" ")
        for i in range(len(list1)):
            string=list1[i]
            if i!=0 :
               newlist+=" "+string[::-1]
            else:
                 newlist=string[::-1]
        return newlist
            
        
        