class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        newset=set()
        def backtracking(k,l,r):
            if len(word)==r:
                return True
            if (len(board)<=k or len(board[0])<=l or k<0 or l<0 or word[r]!=board[k][l] or  (k,l) in  newset):
                return False
            newset.add((k,l))
            res=(backtracking(k,l+1,r+1) or
                backtracking(k,l-1,r+1) or
                backtracking(k-1,l,r+1) or
                backtracking(k+1,l,r+1))
            newset.remove((k,l))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtracking(i,j,0):
                    return True
        return False
    
                
            
                    
