class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 1
        output = []
        new_num = 0
        
        for num in nums:
            
            if num == 0:
                zero_count +=1
            else:
                total *= num
        for i in range(len(nums)):
            if zero_count>=2:
                output.append(0)
                continue
            if zero_count == 0:
                if nums[i] != 0:
                    new_num= total//nums[i]
                    output.append(new_num)
            if zero_count == 1:
                if nums[i] != 0:
                    output.append(0)
                else:
                    output.append(total)



        
        
        return output
