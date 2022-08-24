class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_list = list(str(x))
        itr = int(len(s_list)/2)
        
        isPalindrome = True
        for i, c in enumerate(s_list[:itr]):
            last_ele = i+1
            if s_list[i] != s_list[-last_ele]:
                isPalindrome = False
        
        return isPalindrome