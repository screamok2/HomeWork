import string
import keyword

name = input("enter tne name:")
start_digit = name[0].isdigit()
gg = string.punctuation
gg1 = gg.replace("_","")
if start_digit == True:
    print("не може бути число на початку ")
if " " in name:
    print("не можно використовувати пробіл")
if name.count("_") >1 :
    print("не можно використовувати більше 2х '_'")
if name in keyword.kwlist:
    print("не може бути зареєстрованим словом ")
for element in name:
    if element in string.ascii_uppercase:
        print("не може містити великі літери")
    if element in gg1:
        print("не може містити знаки пунктуації")
