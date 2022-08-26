class Solution:
    def isValid(self, s: str) -> bool:
 
        stack = []

        liststr = list(s)
        
        for c in liststr:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif c == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(c)
                elif c == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        stack.append(c)
            
        return len(stack) == 0