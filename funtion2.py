def noreturn_withargument(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print("*",end=" ")
        print()
noreturn_withargument(5)