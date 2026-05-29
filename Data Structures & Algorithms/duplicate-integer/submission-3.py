class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        this_dicc = {}
        for num in nums:
          if num in this_dicc:
            return True
          else:
            this_dicc[num] = 1
        return False