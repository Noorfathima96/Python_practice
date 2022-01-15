#Task1:

#Input:
#Li1 = [3,4,5,2,7,8,9,10]

#Output:
#Li_odd = [3,5,7,9]
#Li_even = [4,2,8,10]

'''Li = [3,4,5,2,7,8,9,10]
odd=list()
even=list()
for i in Li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)'''

#Task2:

#Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]
    
#Output:
#neg_LI = [-1,-7,-3]
#pos_LI = []
#Zeros = []

'''a=[-1, -7,8,10,20,21,17,28,-3,0,0,]
neg_a=[]
pos_a=[]
zero_a=[]
for i in a:
    if(i>0):
        pos_a.append(i)
    elif(i<0):
        neg_a.append(i)
    else:
        zero_a.append(i)
print(neg_a)
print(pos_a)
print(zero_a)
print("count of negative numbers are",len(neg_a))
print("count of positive numbers are",len(pos_a))
print("count of zeros are",len(zero_a))'''

#Task3:

#Collect a List from user
Li=list()
len=input("length of the list")
for i in range(len):
    x=(int(input("enter the elements of the list")))
    Li.append(x)
    print(Li[i])

          
    



