class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1==text2:
            return len(text1)
        memo={}
        def solve(p1,p2): 
            if (p1,p2) not in memo: 
                if p1>=len(text1) or p2>=len(text2):
                    memo[(p1,p2)]=0      
                else:
                    if text1[p1]==text2[p2]:
                        memo[(p1,p2)]=1+solve(p1+1,p2+1)   
                    else:
                        memo[(p1,p2)]=max(solve(p1+1,p2),solve(p1,p2+1))
            return memo[(p1,p2)]
  
        return solve(0,0)    
        
