list_1= [1,2,3,4,5,6]
size = len(list_1)
size_1= int(size)
print("довжина списку",size_1 )
if size_1 % 2 ==0:
    x=int(size_1/2)
    print("парна")
    list_2 = list_1[0:x]
    list_3 = list_1[x:]
    print([list_2,list_3])
else:
    x = int(size_1 / 2 + 0.5)
    print("непарна")
    list_2 = list_1[0:x]
    list_3 = list_1[x:]
    print([list_2,list_3])