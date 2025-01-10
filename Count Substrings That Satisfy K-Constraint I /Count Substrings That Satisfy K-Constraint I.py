class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        list1=[0,0]
        left=0
        answer=0
        for  i in range(len(s)):
             value=int(s[i])
             list1[value]+=1
             while list1[0]>k and list1[1]>k:
                   list1[int(s[left])]-=1
                   left+=1
             answer+=i-left+1
        return answer
