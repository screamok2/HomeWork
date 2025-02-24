import math

num= int(input("enter the number:"))
while num > 9 :
    num = math.prod(map(int,str(num)))
print(num)