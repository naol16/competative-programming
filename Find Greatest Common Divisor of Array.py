class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a,b=min(nums),max(nums)
        gcd=1
        for i in range(2,a+1):
            if a%i==0 and b%i==0:
                gcd=i
        return gcd
            
        
