n=int(input("Enter the number of values:"))
lis=[]
new=[]
for i in range(n):
    val=int(input("Enter the number:"))
    lis.append(val)
print("List :",lis)
for i in lis:
    if i>0:
        new.append(i)
print("New list :",new)
