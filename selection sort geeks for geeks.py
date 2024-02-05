class Solution: 
    def select(self, arr, i):
        # code here
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[minindex]>arr[j]:
                minindex=j
        return(minindex)
            
            
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            minindex=self.select(arr,i)
            arr[i],arr[minindex]=arr[minindex],arr[i]
                   
