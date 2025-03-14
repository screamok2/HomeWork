import string

def first_world (text):
    text1 = text.replace( ".", " ")
    gg = string.punctuation.replace("'", '')
    text2 = "".join(item for item in text1 if item not in gg)
    text3 = text2.split()
    print(text3[0])

first_world("Hello.World")