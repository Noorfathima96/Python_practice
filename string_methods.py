#middle char of string
a="wikipedia"
b=int((len(a))/2)
print(a[b::1])

#swapcase
a=input("enter the string")
print(a.swapcase())
    
#string concatenate
string_first=input("enter the first string")
string_second=input("enter the second string")
print("the concatenated string is",string_first+' '+string_second)

#title
c=input("enter the string")
print(c.title())

#mutation
s=input("enter the string")
m=int(input("enter the index number"))
new_character=input("enter the new character")
s=s[:m]+new_character+s[m+1:]
print(s)


      
a="wikipedia"
print(a[:2]+a[4:])

