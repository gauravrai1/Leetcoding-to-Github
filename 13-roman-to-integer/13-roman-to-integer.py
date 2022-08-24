class Solution:
    

    def romanToInt(self, s: str) -> int:
        roman = list(s)
        res = 0
        for i, digit in enumerate(roman):
            val_to_add = 0
            if digit == 'M':
                val_to_add = 1000
            if digit == 'D':
                val_to_add = 500
            if digit == 'L':
                val_to_add = 50 
            if digit == 'V':
                val_to_add = 5
            if digit == 'C':
                if i != len(roman)-1:
                    if roman[i+1] == 'D':
                        val_to_add = 400
                        del roman[i+1]
                    elif roman[i+1] == 'M':
                        val_to_add = 900
                        del roman[i+1]
                    else:
                        val_to_add = 100
                else:
                    val_to_add = 100
                
            if digit == 'X':
                if i != len(roman)-1:
                    if roman[i+1] == 'L':
                        val_to_add = 40
                        del roman[i+1]
                    elif roman[i+1] == 'C':
                        val_to_add = 90
                        del roman[i+1]
                    else:
                        val_to_add = 10 
                else:
                    val_to_add = 10 
            if digit == 'I':
                if i != len(roman)-1:
                    if roman[i+1] == 'V':
                        val_to_add = 4
                        del roman[i+1]
                    elif roman[i+1] == 'X':
                        val_to_add = 9
                        del roman[i+1]
                    else:
                        val_to_add = 1
                else:
                    val_to_add = 1
            res = res + val_to_add     
            
        return res
            
                