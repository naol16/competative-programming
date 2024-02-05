class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.summation=[0]
        for num in nums:
            self.summation.append(self.summation[-1]+num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        leftside=self.summation[left]
        rightside=self.summation[right+1]
        return rightside-leftside
