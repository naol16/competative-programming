class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
        new_list=[0]*(n+2)
        length=len(bookings)
        total_sum=0
        for j  in range(length):
            new_list[bookings[j][0]]+=bookings[j][2]
            new_list[bookings[j][1]+1]-=bookings[j][2]
        for  i in range(len(new_list)):
             total_sum+=new_list[i]
             new_list[i]=total_sum
        new_list.pop(0)
        new_list.pop()
        return new_list
                        
            
        