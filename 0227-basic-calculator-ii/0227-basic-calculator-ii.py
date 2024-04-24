class Solution:
    def calculate(self, s: str) -> int:
        # maintain idx        
        # cur_operator
        # if it is / or *, undo the before and add it back again
        
        i = 0
        prev = cur = res = 0
        cur_operation = "+"
        
        while i < len(s):
            # if i is digit
                # parse digit
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i +=1
                i -= 1
                
                if cur_operation == "+":
                    res += cur
                    prev = cur
                    
                if cur_operation == "-":
                    res -= cur
                    prev = -cur
                    
                if cur_operation == "*":
                    # undo
                    res -= prev
                    res += (prev * cur)
                    prev = cur*prev
                if cur_operation == "/":
                    res -= prev
                    res += int(prev / cur)
                    prev = int(prev / cur)
                cur = 0
            # if i is not digit
            elif s[i] != " ":
                # check if it's not white space
                cur_operation = s[i]
            
            i += 1
        return res
        