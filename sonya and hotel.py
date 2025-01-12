a,b=map(int,input().split())
list1=list(map(int,input().split()))
newvalue2=set()
answer=2
for i in range(1,len(list1)):
    if list1[i]-list1[i-1]>2*b:
       answer+=2
    elif list1[i]-list1[i-1]==2*b:
         answer+=1
print(answer)
