'''a=int(input("enter the number"))
fact=1
for i in range(1,a+1):    
    fact=i*fact
print("the factorial of number {} is {}".format(a,fact))'''


def fact(n):
    if (n==0 or n==1):
        return 1
    return n*fact(n-1)

a=int(input("enter the number"))
factorial=fact(a)
print(fact(a))
#print("the factorial of number {} is {}".format(a,fact))


    
