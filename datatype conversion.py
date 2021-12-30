#perimeter of a circle
pi=3.14
radius=4.5
perimeter=int(2*pi*radius)
print("the perimeter of a circle with pi {} and radius {} is {}".format(pi,radius,perimeter))

print('-------------------------')
#Area of a cone
height=5.2
Area=int(1/3*pi*radius*radius*height)
print("the area of a cone with pi {}, radius {} and height {} is {}".format(pi,radius,height,Area))


print('-------------------------')
#data type conversion

#int to other
a=5
print('int value is',a)
print("int to float is",float(a))
print("int to string is",str(a))
print("int to boolean is",bool(a))

print('-------------------------')
#float to other
b=5.5
print('float value is',b)
print("float to int is",int(b))
print("float to string is",str(b))
print("float to bool is",bool(b))

print('-------------------------')
#string to other
c="10"
print('string is',c)
print("string to int is",int(c))
print("string to float is",float(c))
print("string to bool is",bool(c))

print('-------------------------')
#bool to other
d=True
print('boolean is',d)
print("boolean to int is",int(d))
print("boolean to float is",float(d))
print("boolean to string is",str(d))

print('-------------------------')
e=False
print('boolean is',e)
print("boolean to int is",int(e))
print("boolean to float is",float(e))
print("boolean to string is",str(e))
