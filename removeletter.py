class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq={}
        for i in word:
            freq[i] = freq.get(i,0)+1
        newlists=set(freq.values())
        if len(newlists)>2:
           return False
        if len(newlists)==1:
           value=next(iter(newlists))
           return value==1 or len(freq)==1
        maxvalue=max(newlists)
        minvalue=min(newlists)
        #min_max
        count_maxvalue=0
        count_minvalue=0
        for value in freq.values():
            if value==maxvalue:
               count_maxvalue+=1
            else:
                 count_minvalue+=1
        return (count_maxvalue==1 and  maxvalue-minvalue==1) or (count_minvalue==1 and minvalue==1)


                 
          
        

        


        
