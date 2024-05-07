
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(left, right, turn, totalsum1, totalsum2):
            if left == right:
                if turn == "player1":
                    totalsum1 += nums[left]
                else:
                    totalsum2 += nums[left]
                return totalsum1 >= totalsum2
            
            if turn == "player1":
                choose_left = helper(left + 1, right, "player2", totalsum1 + nums[left], totalsum2)
                choose_right = helper(left, right - 1, "player2", totalsum1 + nums[right], totalsum2)
                return choose_left or choose_right
            else:
                choose_left = helper(left + 1, right, "player1", totalsum1, totalsum2 + nums[left])
                choose_right = helper(left, right - 1, "player1", totalsum1, totalsum2 + nums[right])
                return choose_left and choose_right

        return helper(0, len(nums) - 1, "player1", 0, 0)
                      
        
        