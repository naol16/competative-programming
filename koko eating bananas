class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        left=1
        right=max(piles)
        result=right
        while left<=right:
              summation=0
              middle=(left+right)//2
              for i in piles:
                  summation+=(i+middle-1)/middle
                  
              if summation<=h:
                  result=min(result,middle)
                  right=middle-1
              else:
                   left=middle+1
        return result
