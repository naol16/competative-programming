n = int(input())
dictionary={}
for i in range(n):
    num=i+1
    dictionary[num]=[]
    list1=list(map(int,input().split()))
    for i in range(len(list1)):
        if list1[i]==1:
           dictionary[num].append(i+1)
sum=0
for i in range(1,n+1):
    sum+=len(dictionary[i])

print(int(sum/2))
    



