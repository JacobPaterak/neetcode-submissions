class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
       
        s2 = ""
        for char in s:
            if char.isalnum():
                s2 += char
        end = len(s2)-1
        print(s2)
        while end > start:
            if s2[start].lower() != s2[end].lower():
                return False
            end -=1
            start +=1

        return True

