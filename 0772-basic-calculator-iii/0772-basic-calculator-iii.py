class Solution:
    def calculate(self, s: str) -> int:
        op, num = "+", 0
        stack = []
        
        # operator: + - * / ( )
        def helper(op, num): 
            if op == "+":
                stack.append(num)
            if op == "-":
                stack.append(-num)
            if op == "*":
                stack.append(stack.pop()*num)
            if op == "/":
                stack.append(int(stack.pop() /num))
                
        
        # stack (sum it up at once at the end)
        # go through str s
        for i in range(len(s)):
            # if digit -> get all the digit
            if s[i].isdigit():
                num = num *10 + int(s[i])
            if s[i] == "(":
                stack.append(op)
                num = 0
                op = "+"
            # if + - * /  )
            # call helper
            # if (
                # add op
            if s[i] in ["+", "-", "*", "/", ")"]:
                helper(op, num)
                if s[i] == ")":
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    helper(op, num)
                op = s[i]
                num = 0
            # process until not int
            # pop the op
            # process
        helper(op, num)
        # process the last one
        # sum stack
        return sum(stack)