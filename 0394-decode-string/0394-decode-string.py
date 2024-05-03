class Solution:
    def decodeString(self, s: str) -> str:
         list1=[]
         for j in range(len(s)):
             if s[j]!="]":
                list1.append(s[j])
             else:
                  new_string=""
                  while list1[-1]!="[":
                        new_string=list1.pop()+new_string
                  list1.pop()
                  digit=""
                  while list1 and list1[-1].isdigit():
                        digit=list1.pop()+digit
                  list1.append(int(digit)*new_string)
         return "".join(list1)
        