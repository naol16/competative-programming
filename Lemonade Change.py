class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total=[0,0,0]
        for i in range(len(bills)):
            if bills[i]==5:
               total[0]+=1
            elif bills[i]==10:
                 if total[0]>=1:
                    total[0]-=1
                    total[1]+=1
                 else:
                      return False
            elif  bills[i]==20:
                  if total[0]>=1 and total[1]>=1:
                     total[0]-=1
                     total[1]-=1
                  else:
                       if total[0]>=3:
                          total[0]-=3
                       else:
                            return False


        return True
