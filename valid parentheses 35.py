class Solution:
    def isValid(self, s: str) -> bool:
        
        mydict = {')': '(', ']': '[', '}': '{'}
        brackets = list(s)
        stack = []
        for bracket in brackets:
            if bracket in mydict.values():
                stack.append(bracket)
            elif bracket in mydict.keys() and len(stack) == 0:
                stack.append('invalid')
            elif bracket in mydict.keys() and mydict[bracket] == stack[-1]:
                stack.pop(-1)
            elif bracket in mydict.keys() and mydict[bracket] != stack[-1]:
                stack.append('invalid')
        return len(stack) == 0
