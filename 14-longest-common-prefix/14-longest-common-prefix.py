class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comp_word = strs[0]
        strs = strs[1:]
        i = 0
        j = 0
        while i < len(strs):
            chars = list(comp_word)
            word_chars = list(strs[i])
            
            c_len = len(chars)
            l_len = len(word_chars)
            f_len = 0
            if c_len < l_len:
                f_len = c_len
            else:
                f_len = l_len
            new_chars = ""
            while j < f_len:
                if chars[j] == word_chars[j]:
                    new_chars = new_chars + chars[j]
                else:
                    break
                j += 1
            comp_word = new_chars
            j = 0
            i += 1
            
        return comp_word
                    

                
                