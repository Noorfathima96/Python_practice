'''create a dictionary
#{1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
#Extract "bobtn" from above dictionary
#Extract "arbeg" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key "2"'''

a={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(a[3][0][0::2])
print(a[3][2][-1:-6:-1])
print(tuple(a.keys()))
b=a[2]
print("average is",(sum(b)/len(b)))
