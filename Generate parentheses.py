class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        def bactracking(l,r,path):
            if l==r and r==n:
                answer.append(path)
                return
            if l<r or l>n or r>n:
                return
            bactracking(l+1,r,path+'(')
            bactracking(l,r+1,path+')')    
        bactracking(0,0,'')
        return answer
            
