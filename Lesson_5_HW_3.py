import string
name = input("enter the name:")
name1 = name.title()
print(name)
for element in name:
    if element in string.punctuation +" ":
        name1 = name1.replace(element,"")
if len(name1) > 140:
    name2 = name1[:140]
    print("#"+name2)
else:print("#"+name1)
