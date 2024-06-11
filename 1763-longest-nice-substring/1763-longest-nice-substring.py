class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        if len(s)<2:
            return ""

        st=set(s)

        for i,c in enumerate(s):
            if s[i].swapcase() not in st:
                left=self.longestNiceSubstring(s[:i])
                
                
                right=self.longestNiceSubstring(s[i+1:])
                return left if len(left)>=len(right) else right
        return s
            
            