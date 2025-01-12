a,b=map(int,input().split())
list_of_color=list(map(int,input().split()))
length=1
maxvalue=1
for i in range(1,len(list_of_color)):
 
    if list_of_color[i-1]!=list_of_color[i]:
       length+=1
    else: 
         length=1
    maxvalue=max(maxvalue,length)
print(maxvalue)
          
