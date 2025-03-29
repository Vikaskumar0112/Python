# card opration
tup1=(1,2,3,4,6,5,4,7)
print(tup1)
ls=list(tup1)
print(ls)

ls=[]
while(True):
    ch=int(input("enter your choice :"))
    if(ch==1):
        n=int(input("enter the number of data :"))
        for i in range(n):
            data= input("enter the  data :")
            ls.append(data)
        tup1=tuple(ls)
        print(tup1)
    elif(ch==2):
        print(ls)
    elif(ch==3):
        n=int(input("enter the number of data remove :"))
        for i in range(n):
            data=input("enter the data:")
            ls.remove(data)
    elif(ch==4):
        n=int(input("enter the index :"))
        data=input("enter the data : ")
        ls[n]=data
    elif(ch==5):
        n=int(input("enter the number of data :"))
        for i in range(n):
            n1=int(input("enter the number of index :"))
            data=input("Enter the data :")
            ls.insert(n,data)
