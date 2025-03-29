def return_noargument():
    a=10
    b=20
    c=a+b
    d=a*b
    return c,d
x=return_noargument()
add=0
for i in x:
    add=add+i
print(add)