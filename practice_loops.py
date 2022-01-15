'''def print_full_name(first, last):
    print("Hello "+first+' '+ last+"! You just delved into python")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)  '''

def mutate_string(string, position, character):
    l = list(string)
    print(l)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

'''string = input()
l = list(string)
print(l)
    
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print (string)'''
