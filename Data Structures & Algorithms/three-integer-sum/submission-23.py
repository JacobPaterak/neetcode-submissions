class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start = 0
       
        output = []
        print(nums)
        
        
        for i in range(len(nums)):
            start = i +1
            end = len(nums)-1
            if nums[i]>0:
                    break
            if i>0 and nums[i] == nums[i-1]:
                continue
            while start<end:
                total = nums[i] + nums[start] + nums[end]
                if total >0:
                    end-=1
                if total<0:
                    start+=1
                if total == 0:
                    output.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while nums[start] == nums[start-1] and start < end:
                        start+=1
                        
        return output
        
        
        
        
        """
        
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1  
            if(nums[i]>0):
                break
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                
                if (i>0):
                    if(nums[i] == nums[i-1]):
                        break
                if(nums[start] == nums[start+1]):
                    start +=1
                    continue
                if(nums[end] == nums[end-1]):
                    end-=1
                    continue
                if(total) == 0:
                    if(start !=end):
                        output.append([nums[i],nums[start],nums[end]])
                        start+=1 
                        continue
              
                if (total) > 0:
                    end -=1
                if (total) < 0:
                    start +=1
               
        """
      