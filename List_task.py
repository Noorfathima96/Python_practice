#Create an empty list (two ways)
#Concatenate with [5,6,7,8]
#add 8,9,1,5,6,7,8,1 elements to that list
#Find frequency of 8 (count)
#find the mean of the list
#find sum (List) + min + Max 
#Find median of the list
#remove duplicates from list and give output in the format of tuple

a=[]
b=[5,6,7,8]
c=a+b
print("concatenated result is:",c)
d=[8,9,1,5,6,7,8,1]
c.extend(d)
print("list c after adding list d",c)
print("count of 8 is:",c.count(8))
import statistics
x=statistics.mean(c)
print("mean is:",x)
print("sum of list is",sum(c))
print("min value in list is",min(c))
print("max value in list is",max(c))
y=statistics.median(c)
print("median is:",y)
m=set(c)
print("converted list to tuple after removing duplicates",tuple(m))
