class Solution:
    def checkDone(self,lis1,lis2):
        for i in range(len(lis2)):
            if lis2[i] != 0:
                if lis2[i] > lis1[i]:
                    return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        minIndex = (-1,-1)
        minLength = 100001
        start = 0
        end = 0
        tChar = [0 for i in range(0,ord('z')- ord('A')+1)]
        for i in t:
            tChar[ord(i)-ord('A')] += 1
        sChar = [0 for i in range(ord('z')-ord('A')+1)]
        while end <= len(s):
            if self.checkDone(sChar,tChar):
                if minLength > end - start:
                    minIndex = (start,end)
                    minLength = end - start
                sChar[ord(s[start])-ord('A')] -= 1
                start += 1
            else:
                if end == len(s):
                    break
                sChar[ord(s[end])-ord('A')] += 1
                end += 1
        if minIndex == (-1,-1):
            return ""
        else:
            return s[minIndex[0]:minIndex[1]]
