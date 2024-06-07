class Solution:
    def splitString(self, s: str) -> bool:
        cur = []
        possible = False
        def backtrack(i):
            # print('cur =', cur)
            nonlocal possible
            if i == len(s):
                possible = (possible or (len(cur) > 1) and (cur[-2] - cur[-1] == 1))
                return
            
            if len(cur) > 1 and cur[-2] - cur[-1] != 1:
                return
            
            for j in range(i + 1, len(s) + 1):
                cur.append(int(s[i:j]))
                backtrack(j)
                cur.pop()
        
        backtrack(0)
        return possible
        