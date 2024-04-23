class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for i in s:
            print(stack)
            if i=="(":
               stack.append(0)
            else:
                 a=stack.pop()
                 stack[-1]+=max(1,2*a)
        return stack.pop()
        
        