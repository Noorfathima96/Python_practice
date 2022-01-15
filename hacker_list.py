'''if __name__ == '__main__':
 N = int(input())
    a=[]
    a.insert(0,5)
    a.insert(1,10)
    a.insert(0,6)
    print(a)
    a.remove(6)
    a.append(9)
    a.append(1)
    a.sort()
    print(a)
    a.pop()
    a.reverse()
    print(a)'''

def is_leap(year):
    if (year%100==0):
        if(year%400==0):
           return True
        else:
            return False
    elif(year%4==0):
        return True
    else:
        return False
year = int(input())
print(is_leap(year))
