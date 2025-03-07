n=int(input("enter the number"))
cnt=0
i=2
while(i<n):
    if(n%i==0):
        cnt+=1
    i+=1
if(cnt==0):
    print("no is prime")
else:
    print("not prime")