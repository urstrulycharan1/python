p=int(input("principal amount:"))
t=float(input("enter the period of time in months:"))
r=float(input("enter the rate of interset"))
si=(p*t*r)/100
print(si)
emi=(p+si)/(t*12)
print(emi)