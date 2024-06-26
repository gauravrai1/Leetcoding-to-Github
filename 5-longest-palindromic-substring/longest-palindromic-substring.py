class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        res = ""
        resLen = 0

        for i in range(len(s)-1):
            
            # odd 
            l, r = i, i
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
                if r-l+1 > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        
        return res