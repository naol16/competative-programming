class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        low,high=1,n
        while low<high:
              middle=(low+high)//2
              if isBadVersion(middle):
                 high=middle
              else:
                   low=middle+1
        return high
        
