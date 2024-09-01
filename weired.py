input1=int(input())
for i in range(input1):
    num1=int(input())
    list1=list(map(int,input().split()))
    list1.sort(reverse=True)
    totalsum=list1[0]
    y=True
    newlist=[]
    if  len(list1)%2==1:
        num=len(list1)//2+1
    else:
         num=len(list1)//2
        
  
    for i in range(num):
        newlist.append(list1[i])
        newlist.append(list1[len(list1)-i-1])
    for i in range(1,len(newlist)):
        if newlist[i]==totalsum:
           y=False
           print('NO')
           break
        else:
             totalsum+=newlist[i]
       
    if y:
       print('YES')
       if len(list1)%2==1:
          newlist.pop()
       print(*newlist)
