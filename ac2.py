a=int(input("enter numerator:"))
b=int(input("enter denominator:"))

if a%b == 0:
    print(str(a)+"is divisible by" +str(b))
else:
    print(str(a)+"is not divisible by" +str(b))