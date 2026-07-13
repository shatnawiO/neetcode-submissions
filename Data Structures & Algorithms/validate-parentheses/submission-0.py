class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetopen = {')':'(','}':'{',']':'['}

        for char in s:
            if char in closetopen:
                if len(stack)>0 and stack[-1] == closetopen[char]:
                    stack.pop()
                else:
                    return False    
            else:
                stack.append(char)
        return True if not len(stack)>0 else False            
        