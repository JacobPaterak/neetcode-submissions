class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        
        
        for i in range(len(nums)):
            numbers[nums[i]] = i
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in numbers:
                if i != numbers.get(tar):
                    return[i, numbers.get(tar)]
            tar = 0