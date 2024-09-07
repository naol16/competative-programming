
input1=int(input())
for _ in range(input1):
    string1=input()
    length=len(string1)//2
    if string1[0:length]==string1[length:len(string1)]:
       print("YES")
    else:
         print("NO")
