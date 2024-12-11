class Solution:
    def compress(self, chars: List[str]) -> int:
        write=0
        left=0
        newstring=''
        for right in range(len(chars)):
            
            if right+1==len(chars)  or chars[right]!=chars[right+1]:
               chars[write]=chars[left]
               write+=1
               amount=right+1-left
               if amount>1:
                  newstring=list(str(amount))
                  for i  in newstring:
                      chars[write]=i
                      write+=1
               left=right+1
        return write
