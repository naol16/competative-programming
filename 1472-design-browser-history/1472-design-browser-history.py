class Node:
      def __init__(self, homepage: str):
          self.homepage=homepage
          self.next=None
          self.prev=None
      # self.head=None
      # self.current=None

class BrowserHistory:
    

    def __init__(self, homepage: str):
        self.page=Node(homepage)
    def visit(self, url: str) -> None:
        self.page.next=Node(url)
        self.page.next.prev=self.page
        self.page=self.page.next
    
        
        
        

    def back(self, steps: int) -> str:
        #moving back ward x starting from last element
        x=steps
        while self.page.prev and x>0:
              self.page=self.page.prev
              x-=1
              
        return self.page.homepage 
        
        

    def forward(self, steps: int) -> str:
        #moving forward x steps from the first element
        y=0
        while self.page.next and steps>y:
              self.page=self.page.next
              y+=1
        return self.page.homepage
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)