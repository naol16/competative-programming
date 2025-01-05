input1=int(input())
for i in range(input1):
    list1=list(map(int,input().split()))
    list1.sort()
    answer=list1[0]*list1[2]
    print(answer)
