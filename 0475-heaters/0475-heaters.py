class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # winter is coming   
        # our first job is to find the  standard heater 
        # with in fixed   warm radius   to warm all the houses 
        # we are supposed to find  the max differnce  between the elements 
       
        houses.sort()
        heaters.sort()
        left, right = 0, max(max(heaters), max(houses))

        while left < right:
            middle = (left + right) // 2
            good_radius = True

            i = 0
            j = 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= middle:
                    i += 1
                else:
                    j += 1
                    if j == len(heaters):
                        good_radius = False
                        break

            if good_radius:
                right = middle
            else:
                left = middle + 1

        return left

        