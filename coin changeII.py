class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def backtrack(i, remaining):
            # Base cases
            if remaining == 0:
                return 1  # Found a valid combination
            if remaining < 0 or i == len(coins):
                return 0 
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            use_coin = backtrack(i, remaining - coins[i])
            skip_coin = backtrack(i + 1, remaining)
    
            memo[(i, remaining)] = use_coin + skip_coin
            return memo[(i, remaining)]
        
        return backtrack(0, amount)
