def simple_interest(p,n,r=5):
    si=(p*r*n)/100
    return si


principal=float(input("enter principal amount"))
time=float(input("enter time in year"))
result=simple_interest(principal,time)
print("simple interest rate:",result)