def strstr(haystack,needle):
    h=len(haystack)
    n=len(needle)
    if(h<n):
         return(-1)
    elif(n==0):
         return(0)
    else:
       for start in range(h-n+1):
           if(haystack[start:start+n]==needle):
               return start
haystack=input("enter the main string:")
needle=input("enter the substring:")
print(strstr(haystack,needle))

    
