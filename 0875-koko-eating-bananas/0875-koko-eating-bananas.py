class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest=1
        highest=max(piles)
        def checker(num):
            current=0
            for pile in piles:
                current+=math.ceil(pile/num)
            return current<=h
        while lowest<highest:
              middle=(lowest+highest)//2
              if checker(middle):
                 highest=middle
              else:
                   lowest=middle+1
        return lowest
                    
                
        