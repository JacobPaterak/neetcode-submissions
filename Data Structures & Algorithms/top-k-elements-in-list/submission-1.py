class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            numbers[num] = 1 + numbers.get(num,0)
        for num in numbers:
          freq[numbers[num]].append(num)
        values = []
        i = len(freq)-1

        for i in range( i,0,-1):
         if freq[i] != [] and k>0:
          for n in freq[i]:
            values.append(n)
            k-=1
        return values