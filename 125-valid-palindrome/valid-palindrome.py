class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(ch for ch in s if ch.isalnum())
        if len(s) == 0:
            return True
        middle = len(s) // 2
        # print("string", s)
        # print("middle", middle)
        startptr = 0
        endptr = -1
        while startptr < middle:
            # print(startptr, endptr)
            # print(s[startptr], s[endptr])
            if s[startptr] == s[endptr]:
                startptr += 1
                endptr -= 1
                continue
            else:
                return False
        return True
