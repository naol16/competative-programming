num1=int(input())
for i in range(num1):
    num=int(input())
    copliment=num&-num
    while (num==copliment or (num&copliment)==0):
            copliment+=1
    print(copliment)
 
 
    
    
