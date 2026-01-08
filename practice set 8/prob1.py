def greater(a, b, c):
    if(a>b and a>c):
     return a
    elif(b>a and b>c):
       return b
    elif(c>a and c>b):
       return c
    
a=1
b=5
c=4

print(greater(a, b, c))
