import math;
n1=float(input("Enter a number"))
n2=float(input("Enter b number"))
print("Difference is ",abs(n1-n2))
if abs(n1-n2)<=0.001:
    print("close")
else:
    print("not close")
