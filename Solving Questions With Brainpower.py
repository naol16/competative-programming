class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo={}
        def backtrack(start):
            if start >= len(questions):
                return 0
            if start in memo:
                return memo[start]
            points_if_solve = questions[start][0] + backtrack(start + questions[start][1] + 1)

            points_if_skip = backtrack(start + 1)
            memo[start] = max(points_if_solve, points_if_skip)

            return memo[start]

        return backtrack(0)

            
