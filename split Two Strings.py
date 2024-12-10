class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        left=0
        left1=len(b)-1
        right1=0
        right=len(a)-1
        while left < right:
            if a[left]==b[right]:
                left+=1
                right-=1
            else:
                break
 
        while right1<left1:
            if a[left1]==b[right1]:
                left1-=1
                right1+=1
            else:
                break
 
        ans1=a[:left]+a[left:right+1]+b[right+1:]
        ans2=a[:left]+b[left:right+1]+b[right+1:]
        ans3=b[:right1]+a[right1:left1+1]+a[left1+1:]
        ans4=b[:right1]+b[right1:left1+1]+a[left1+1:]
        result=False
        
        if ans1==ans1[::-1]:
            result=True
 
        if ans2==ans2[::-1]:
            result=True
 
        if ans3==ans3[::-1]:
            result=True
 
        if ans4==ans4[::-1]:
            result=True
 
        return(result)
