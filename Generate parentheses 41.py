class solution(object):
    def generateparenthesis(self,n):
        result=[]
        self.generateparenthesisutil(n,n,"",result)
        return result
    def generateparenthesisutil(self,left,right,temp,result):
        if left==0 and right==0:
            result.append(temp)
            return
        if(left>0):
            self.generateparenthesisutil(left-1,right,temp+'(',result)
        if(right>left):
            self.generateparenthesisutil(left,right-1,temp+')',result)
n=int(input("no.of parenthesis:"))
ob=solution()
print(ob.generateparenthesis(n))
