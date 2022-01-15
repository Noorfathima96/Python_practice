#HCF of two numbers
'''a=int(input("enter first number"))
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
print("HCF of two numbers {} and {} is {}".format(a,b,max(c)))'''

#LCM of two numbers
def hcf(a,b):
    s1=set()
    for i in range(1,a+1):
        if(a%i==0):
            s1.add(i)
    s2=set()
    for j in range(1,b+1):
        if(b%j==0):
            s2.add(j)
    c=s1.intersection(s2)
    return max(c)

x=int(input("enter first number"))
y=int(input("enter second number"))
product=x*y
LCM=product/hcf(x,y)
print("LCM of two numbers {} and {} is {}".format(x,y,LCM))



    
