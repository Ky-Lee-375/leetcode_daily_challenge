class Solution:
    def letterCombinations(self, digits: str) -> List[str]:         
        if digits == '':
            return []
        
        digit_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        output =list(digit_dict[digits[0]]) 
        
        for digit in digits[1:]:
            temp= []
            for str1 in output:
                for str2 in list(digit_dict[digit]):
                    temp.append(str1+str2)
            output = temp
                    
        return output