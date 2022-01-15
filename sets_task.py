#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences(difference)
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

a=set()
b=set()
c={7,8,9,1,2,3,4,5,0}
d={4,5,6,0}
a.update(c)
b.update(d)
print(a)
print(b)
print(b.issubset(a))
print(b.issuperset(a))
'''a.intersection_update(b)
print(a)'''
a.discard(8)
b.discard(8)
a.difference_update(b)
print(a)

a.discard(0)
b.discard(0)
x=a.union(b)
print(x)

