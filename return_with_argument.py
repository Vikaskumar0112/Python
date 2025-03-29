def return_with_argument(a,b):
    c=a+b
    d=a*b
    return c,d
x=return_with_argument(10,20)
add=0
for i in x:
    add=add+i
print(add)