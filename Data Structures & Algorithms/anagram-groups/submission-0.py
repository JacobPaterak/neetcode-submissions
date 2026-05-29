class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        if len(strs) == 1:
            return [strs]
       
        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1
            
            res[tuple(count)].append(str)
        print(res)
        return list(res.values())