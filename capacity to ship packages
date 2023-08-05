class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l,r=max(weights),sum(weights)
        def checking(weights,capacity,days):
            capacityload=0
            days2=1
            for i in weights:
                 capacityload+=i
                 if capacityload>capacity:
                     days2+=1
                     capacityload=i
            return days>=days2
        while l<r:
              mid=(l+r)//2
              if checking(weights,mid,days):
                 r=mid
              else:
                   l=mid+1
        return l
                 
