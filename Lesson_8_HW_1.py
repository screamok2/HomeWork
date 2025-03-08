def add_one(some_list):
    some_list1= int("".join(str(i) for i in some_list))
    some_list2 = str(some_list1 + 1)
    some_list3 = [int(x) for x in str(some_list2)]
    print(some_list3)
a = [1,2,3,4]
add_one(a)
#assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
#assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
#assert add_one([0]) == [1], 'Test3'
#assert add_one([9]) == [1, 0], 'Test4'
#print("ОК")