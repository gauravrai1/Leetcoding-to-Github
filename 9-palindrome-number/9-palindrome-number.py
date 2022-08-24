class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_list = list(str(x))
        itr = int(len(s_list)/2)
        
        isPalindrome = True
        if x<0:
            isPalindrome = False
        else:    
            rev = int(str(x)[::-1])
            if x != rev:
                isPalindrome = False
        
        return isPalindrome