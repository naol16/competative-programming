class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        left,right=0,len(cardPoints)-k
        totalsum=sum(cardPoints[right:])
        result=totalsum
        while right<len(cardPoints):
              totalsum=totalsum+cardPoints[left]-cardPoints[right]
              result=max(result,totalsum)
              left+=1
              right+=1
        return result
              
                
              
              