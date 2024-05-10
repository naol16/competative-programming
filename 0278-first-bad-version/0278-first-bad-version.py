# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        highest=n
        lowest=1
        while lowest<=highest:
              middle=(highest+lowest)//2
              if isBadVersion(middle):
                 highest=middle-1
              else:
                   lowest=middle+1
        return lowest
                 
        