import random;
a=[]
for i in range(1,34):
    b=random.randrange(1,100)
    a.append(b)
print(a)
s=0;
for i in range(20):
    s=s+a[i];
print("Average",s/20)
print(sorted(a))
print("The smallest number in list:",min(a))
print("The largest number in list:",max(a))
a.remove(min(a))
a.remove(max(a))
print("The second largest number in list:",max(a))
print("The second smallest number in list:",min(a))
b=[]
b=sorted(a)
print(b)
for i in b:
    if i%2==0:
        print(i)
