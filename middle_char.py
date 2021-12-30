#middle char of string

a=input("enter a string:")
b=int((len(a))/2)
if(int(len(a)%2)==0):
    print("middle char are {},{}".format(a[b-1],a[b]))
else:
    print(a[b])
