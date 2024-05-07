class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxSize=maxSize
        self.count=0
        

    def push(self, x: int) -> None:
        if self.count<self.maxSize:
           self.stack.append(x)
           self.count+=1
        
        

    def pop(self) -> int:
        if not self.stack:
           return -1
        value=self.stack.pop()
        self.count-=1
        return value
        

    def increment(self, k: int, val: int) -> None:
        if self.stack:
           if k>=len(self.stack):
              for i in range(len(self.stack)):
                  self.stack[i]+=val
           else:
                for i in range(0,k):
                    self.stack[i]+=val
                 
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)