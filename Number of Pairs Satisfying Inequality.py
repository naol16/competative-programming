class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
          l = len(nums1)
          new_list = []
          res = 0
          for i in range(l):
              diff2 = nums1[i] - nums2[i]
              cand= diff2 + diff
              index = bisect.bisect_right(new_list, cand)
              res += index
              bisect.insort(new_list, diff2)
          return res
        
