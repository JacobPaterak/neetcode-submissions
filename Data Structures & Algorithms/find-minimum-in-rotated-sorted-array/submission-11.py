class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] > nums[len(nums)-1]:
            mid = (len(nums)//2)
            l = 0
            r = len(nums)-1
            while l!=r:
                if nums[mid] > nums[l]:
                    l = mid
                    mid = (r + l) //2
                    continue
                if nums[mid] < nums[l]:
                    r = mid
                    mid = (r+l)//2
                    continue
                if mid == l:
                    return nums[r]
                else:
                    return nums[r]
                    
        else:
            return nums[0]