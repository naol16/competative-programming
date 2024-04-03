class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        min_=float('inf')
        max_=0
        for cap, start, end in trips:
            max_=max(max_,end)
        
        pref=[0]*(max_+2)

        for cap, start, end in trips:
            pref[start]+=cap
            pref[end]-=cap
        
        for i in range(1, max_+1):
            pref[i]+=pref[i-1]
        
        for num in pref:
            if num>capacity:
                return False
        return True
   