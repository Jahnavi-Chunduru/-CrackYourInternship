def calculate(self, s):
    stack, sign, num = [], "+", 0
    
    for i in range(len(s)):
        if s[i].isdigit():
            num = num*10 + int(s[i])
            
        if s[i] in "+-*/" or i == len(s)-1:
            if sign == "+":
                stack.append(num)
            elif sign == "*":
                stack[-1] = stack[-1]*num
            elif sign == "/":
                stack[-1] = int(stack[-1]/num)
            elif sign == "-":
                stack.append(-num)    
                
            num = 0
            sign = s[i]

    return sum(stack)
