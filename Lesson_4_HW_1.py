
list_1 = [0,1,0,12,3]
list_2 = [1, 0, 13, 0, 0, 0, 5]
list_3 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


list_1.sort(key=lambda x: x == 0)
print(list_1)

list_2.sort(key= lambda x:x==0)
print(list_2)

list_3.sort(key= lambda x: x==0)
print(list_3)


# довелось трошки погуглити :))