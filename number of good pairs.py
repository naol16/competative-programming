 dict1={

        }
        sum=0
        for i in range(len(nums)):
            if nums[i] in dict1:
               dict1[nums[i]]+=1
            else:
                 dict1[nums[i]]=1
        
        for j in dict1.values():
            sum+=(j * (j - 1)) // 2
        return sum

              
        
