a=int(input("enter a number"))
num=a
s=0
while(a>0):
    r=a%10
    s=s+(r*r*r)
    a//=10
if(num==s):
    print("{} is an armstrong number".format(num))
else:
    print("{} is not an armstrong number".format(num))
 
