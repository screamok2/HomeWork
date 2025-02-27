def second_index(text, some_str):
    first_index = text.find(some_str)
    second_index = text.find(some_str, first_index+1)
    if second_index <= 0:
        second_index = None
    print(second_index)
a = str(input("enter 1:"))
b = str(input("enter 2:"))
second_index (a, b)
