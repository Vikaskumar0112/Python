for i in range(5):
    for k in range(5-(i+1)):
        print("",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(4,0,-1):
    for k in range(5-i):
        print("",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()