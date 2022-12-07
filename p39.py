n=int(input("enter the number:"))
n1=0
n2=1
nextnum=n1+n2
print(n1)
print(n2)
print(nextnum)
for i in range (3,n+1):
    n1=n2
    n2=nextnum
    nextnum=n1+n2
    print(nextnum,end="  ")