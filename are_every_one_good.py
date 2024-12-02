dictionary={}
a=int(input())
string1=input()
string2=set(string1)
string3=''
left=0
right=0
value=0
answer=len(string1)
while right<len(string1):
      newstring3=string1[right]
      if newstring3  in dictionary:
         dictionary[newstring3]+=1
      else:
           dictionary[newstring3]=1
 
      while len(dictionary)==len(string2):
            answer=min(right-left+1,answer)
            if dictionary[string1[left]]==1:
                  del dictionary[string1[left]]
            else:
                 dictionary[string1[left]]-=1
            left+=1
      right+=1
print(answer)
