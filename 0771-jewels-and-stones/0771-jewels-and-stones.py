class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=set(jewels)
        count=0
        for string in stones:
            if string in jewels:
               count+=1
        return count
        