class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        s = 0
        
        def dfs(i):
            nonlocal s, target
            if s == target:
                ans.append(cur.copy())
                return
            if s > target or i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                s += candidates[j]
                dfs(j)
                cur.pop()
                s -= candidates[j]
        
        dfs(0)
        return ans
