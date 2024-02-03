 num=0
        
        for string in  operations:
            if string =="--X" or string=="X--":
               num-=1
            elif string=="++X" or string=="X++":
                 num+=1
        return num
