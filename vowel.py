a=(input("input a string"))
b=int((len(a))/2)
if(int(len(a)%2)==0):
    Li=[a[b-1],a[b]]
    print("middle char are",Li)
    if(a[b-1] and a[b]== 'a' or a[b-1] and a[b]== 'e' or a[b-1] and a[b]== 'i' or a[b-1] and a[b]==
       'o' or a[b-1] and a[b]== 'u'):
        print("both are vowels")
    elif(Li[0]=='a' or 'e' or 'i' or 'o' or 'u'):
        print("{} is an vowel".format(a[b-1]))
    elif(Li[1]=='a' or 'e' or 'i' or 'o' or 'u'):
        print("{} is an vowel".format(a[b]))
    else:
        print('not an vowel')
else:
    c=a[b]
    print("middle char is",c)
    if(a[b]== 'a' or 'e' or 'i' or 'o' or 'u'):
        print('is an vowel')
    else:
        print('not an vowel')
