ls=12,2,6,8,84,54,17
for i in range(len(ls)):
    for j in range(0,len(ls)-i-1):
        if (ls[j]>ls[j+1]):
            ls[j],ls[j+1]=ls[i+1],ls[j]
print(ls)