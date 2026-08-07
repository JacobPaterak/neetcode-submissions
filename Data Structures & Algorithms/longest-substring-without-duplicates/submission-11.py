class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        counter = 0
        l = 0
        r = -1
        chars = set()

            
        for i in range(len(s)):
            if s[i] not in chars:
                r +=1
                chars.add(s[i])
                
            else:
                while s[i] in chars:
                    if s[l] in chars:
                        chars.remove(s[l])
                    l+=1
                chars.add(s[i])
                
           
            max_len = max(max_len,len(chars))    
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
