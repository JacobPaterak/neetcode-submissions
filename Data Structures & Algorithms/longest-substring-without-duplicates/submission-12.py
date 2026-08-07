class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        counter = 0
        l = 0
        chars = set()

            
        for i in range(len(s)):
                
            while s[i] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[i])

            max_len = max(max_len,i-l + 1 )    
        
        return max_len
        
        
        #for char in s:
         #   if char not in chars:
          #      chars.add(char)
           #     counter = counter + 1
            #    max_len = max(max_len, counter)
            #else:
             #   counter = 1
              #  chars.clear()
               # chars.add(char)
        #return max_len
