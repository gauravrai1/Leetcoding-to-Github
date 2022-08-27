class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       
        new_li = []
        
        i = 0
        
        while(i <= len(haystack)-len(needle)):
            new_li.append(haystack[i:len(needle)+i])
            i += 1
        
        for j, n in enumerate(new_li):
            if n == needle:
                return j
        
        return -1
            
            