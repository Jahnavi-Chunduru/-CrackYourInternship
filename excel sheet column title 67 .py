def title_convert(n):
    return title_convert((n-1)//26)+\
           chr(ord('A')+(n-1)%26) if n else ''
n=int(input("enter the column number:"))
print(title_convert(n))
