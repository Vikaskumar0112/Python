# #wap to add first 10 natural number
# n=int(input("enter the number"))
# i=1
# add_natural_number=0
# while(i<=n):
#     add_natural_number=add_natural_number+i
#     i+=1
# print("addition=",add_natural_number)
#wap to add first 10 natural number
n=int(input("enter the number"))

i=1
esum=0
osum=0
while(i<=n):
    if(i%2==0):
        esum=esum+i
    else:
        osum=osum+i
        