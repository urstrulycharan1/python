def Happy(num):
    r=sum=0
    while num>0:
        r=num%10
        sum=sum+(r*r)
        num=num//10
    return sum
num=int(input('Enter the number:'))
result=num
while result!=1 and result!=4:
    result=Happy(result)
if result==1:
    print(num,'is Happy Number')
elif result==4:
    print(num,'is not a Happy Number')