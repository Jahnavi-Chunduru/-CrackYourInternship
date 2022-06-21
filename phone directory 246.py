class Solution:
   def displayContacts(self, n, contact, s):
       contact=list(set(contact))
       st=""
       output=[]
       for i in range(len(s)):
           st+=s[i]
           temp=[]
           l=len(st)
           for j in contact:
               if j[:l]==st:
                   temp.append(j)
           if bool(temp)==False:
               output.append(list([0]))
           else:
               temp.sort()
               output.append(temp)
       return output
