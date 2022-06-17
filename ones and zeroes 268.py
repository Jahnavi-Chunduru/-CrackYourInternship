class Solution(object):
    def recur(self,m,n,i):
        if(i==len(self.num)):
            return 0
        if(m==0 and n==0):
            return 0
        if(self.mem[m][n][i] != -1):
            return self.mem[m][n][i]
            
        ones, zeros = 0,0
        for c in self.num[i]:
            if(int(c)==1):
                ones+=1
            else:
                zeros+=1
                
        if(m-zeros < 0 or n-ones < 0):
            self.mem[m][n][i] = self.recur(m,n,i+1)
            return self.mem[m][n][i]
        
        self.mem[m][n][i] = max(self.recur(m-zeros,n-ones,i+1)+1,self.recur(m,n,i+1))
        return self.mem[m][n][i]
            
        
        
    def findMaxForm(self, strs, m, n):
        self.mem = [[[-1]*(len(strs)+1) for i in range(n+1)] for j in range(m+1)]
        self.num = strs
        return self.recur(m,n,i=0)
