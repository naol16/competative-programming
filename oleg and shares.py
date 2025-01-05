a,b=map(int,input().split())
list1=list(map(int,input().split()))
total=0
output=True
list1.sort()
for i in range(1,a):
    value=list1[i]-list1[0]
    if value%b!=0:
       output=False
       break
    else:
         total+=value//b
if output:
   print(total)
else:
     print(-1)
