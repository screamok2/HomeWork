def correct_sentence(text):
    b =text.capitalize()
    if b[-1] == ".":
        print(b)
    elif b[-1] != ".":
        c = b + "."
        print(c)
a = str(input("enter:"))
correct_sentence(a)
