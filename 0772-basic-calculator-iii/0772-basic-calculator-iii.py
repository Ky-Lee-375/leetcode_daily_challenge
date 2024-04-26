class Solution:
    def calculate(self, s: str) -> int:
        # op, num
        # stack
        op, num = "+", 0
        stack = []
        
        # helper(op, num)
        # put it into stack
        def helper(op, num):
            if op == "+":
                stack.append(num)
            if op == "-":
                stack.append(-num)
            if op == "*":
                res = stack.pop()
                stack.append(res*num)
            if op == "/":
                res = stack.pop()
                stack.append(int(res/num))
        
        # process the number
        # process case by case
        # isdigit()
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if s[i] == "(":
                stack.append(op)
                num = 0
                op = "+"
            if s[i] in ["+", "-", "*", "/", ")"]:
                helper(op, num)
                if s[i] == ")":
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    helper(op, num)
                num = 0
                op = s[i]
        helper(op, num)
        return sum(stack)
                    
                