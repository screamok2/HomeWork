import random

new_range = range(0 , 100)
x = random.randint(3 , 10)
numbers = list(random.sample(new_range, x))
print("кількість елементів :", x)
print("рандомний список:" , numbers)

new_number_1 = numbers [0]
new_number_2 = numbers [2]
new_number_3 = numbers [-2]
new_list = [new_number_1, new_number_2, new_number_3]
print("новий список:" , new_list)