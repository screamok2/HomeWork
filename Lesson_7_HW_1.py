def say_hi (name, age):
    print(f"Hi. My name is {name.capitalize()} and I'm {age} years old")
a = input("enter the name:")
b = int(input("enter the age:"))
say_hi( a, b)