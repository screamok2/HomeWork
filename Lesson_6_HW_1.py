import string
name = input("input 2 letters:")
x1 = name[0]
x2 = name[1]
z1 = string.ascii_letters.find(x1)
z2 = string.ascii_letters.find(x2)
print(string.ascii_letters[z1:z2+1])
