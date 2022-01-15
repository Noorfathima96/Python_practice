#Task 3
'''a=int(input("enter a number"))
if(a%3==0 and a%5==0):
    print("Fizzbuzz")
elif(a%3==0):
    print("Fizz")
elif(a%5==0):
    print("buzz")
else:
    print("Invalid number")'''

#Task 4
mark=int(input("enter the mark"))
if(0<mark>100):
    print("Invalid mark")
else:
    print("Valid mark")
if(mark>50):
    print("Pass mark")
else:
    print("Fail mark")
if(90<=mark<=100):
    print("A")
elif(80<=mark<=89):
    print("B")
elif(70<=mark<=79):
    print("C")
elif(60<=mark<=69):
    print("D")
elif(50<=mark<=59):
    print("E")

#Hacker rank practice program
n = int(input("enter a number"))
if(n%2==1):
    print("Weird")
elif(n%2==0 and 2<=n<=5):
    print("Not Weird")
elif(n%2==0 and 6<=n<=20):
    print("Weird")
elif(n%2==0 and n>20):
    print("Not Weird")

