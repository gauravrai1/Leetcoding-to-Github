class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opstack = []
        operators = ["+","-","*","/"]
        while len(tokens) > 1:
            # print("tokens before", tokens)
            # print("opstack before", opstack)

            if tokens[-1] in operators and tokens[-2] not in operators and tokens[-3] not in operators:
                val = self.resolveEq(tokens[-3], tokens[-2], tokens[-1])
                tokens.pop()
                tokens.pop()
                tokens.pop()
                tokens.append(val)
            else:
                opstack.append(tokens.pop())

            
            if len(tokens) < 3:
                # print("less")
                while not tokens[-1] in operators and len(opstack)>0:
                    # print("added ", opstack[-1])
                    tokens.append(opstack.pop())
            
        #     print("tokens after", tokens)
        #     print("opstack after", opstack)

        # print("opstack", opstack)
        return int(tokens[0])

    def resolveEq(self, op1, op2, op) -> str:
        num1 = int(op1)
        num2 = int(op2)
        res = 0
        if op == "+":
            res = num1 + num2
        elif op == "-":
            res = num1 - num2
        elif op == "*":
            res = num1 * num2
        else:
            sign = -1 if (num1 < 0) ^ (num2 < 0) else 1
            res = sign * (abs(num1) // abs(num2))
        return str(res)