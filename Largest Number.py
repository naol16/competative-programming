class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #  we will arrange the numbers based on the  remainder of each numbers
        #it  is stating  we are going to compare two numbers only
        # so in the custom comaprtor function we will do the comparsion  for two parts of the element not the all part
        def customcompartor(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        newarray=[str(i) for i in nums]
        newarray.sort()
        newarray.reverse()
        newarray.sort(key=cmp_to_key(customcompartor))
        if newarray[0]=="0":
            return "0"
        return ''.join(newarray)
