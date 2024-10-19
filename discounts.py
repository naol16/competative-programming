input1=int(input())
for i in range(input1):
    a=int(input())
    maximum=0
    sum_of_two=0
    sum_of_three=0
    for i in range(1,a+1):
        if i%2==0:
           sum_of_two+=i
    for i in range(1,a+1):
        if i%3==0:
            sum_of_three+=i
    
       
    if sum_of_two>sum_of_three:
       maximum=2
    else:
         maximum=3
    
    print(maximum)
