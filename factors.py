'''a=int(input("enter the number"))
for i in range(1,a+1):
    if(a%i==0):
        print(i)'''


a=int(input("enter first number"))
s1=set()
for i in range(1,a+1):
    if(a%i==0):
        s1.add(i)
#print(s1)

b=int(input("enter second number"))
s2=set()
for j in range(1,b+1):
    if(b%j==0):
        s2.add(j)
#print(s2)
c=s1.intersection(s2)
print("HCF of numbers {} and {} is {}".format(a,b,max(c)))

