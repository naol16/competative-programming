class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans=[] 
        board=[['.' for i in range(n)]for j in range(n)] 
        pos=[] 
 
        def bac(idx,board): 
            if idx>=n: 
                temp=["".join(x) for x in board] 
                self.ans.append(temp) 
                return  
 
            for i in range(n): 
                f=1 
                if idx>0: 
                    for p in pos: 
                        if p[0]==i or abs(i-p[0]) == abs(idx-p[1]): 
                            f=0 
                            break 
 
                if not f: 
                    continue 
 
                board[i][idx]='Q' 
                pos.append([i,idx]) 
                bac(idx+1,board) 
                board[i][idx]='.' 
                pos.pop() 
 
 
        bac(0,board) 
 
        return self.ans
        