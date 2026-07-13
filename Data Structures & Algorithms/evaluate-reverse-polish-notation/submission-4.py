class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def calulation(num1:int,num2:int,eq:str)->int:
            if eq=='+':
                return num1 + num2
            if eq == '-':
                return num1-num2 
            if eq == '*':
                return num1*num2   
            if eq =='/':
                return int(num1 / num2) 
        listt = ['+','-','*','/']
        for index,token in enumerate(tokens):
            if token not in listt:
                stack.append(int(token))
            elif token in listt:
                     b = stack.pop()
                     a = stack.pop()
                     k = calulation(int(a),int(b),token)
                     stack.append(k)
        return int(stack[0])            



        