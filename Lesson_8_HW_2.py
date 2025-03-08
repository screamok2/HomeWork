import string
from copy import deepcopy

def is_palindrome(text):
    text1 = text.lower()
    for element in text1:
        if element in string.punctuation + " ":
            text1 = text1.replace(element, "")
    text2 = list(text1)
    text3 = deepcopy(text2)
    text3.reverse()
    print(text2 == text3)

is_palindrome("A man, a plan, a canal: Panama")

#assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
#assert is_palindrome('0P') == False, 'Test2'
#assert is_palindrome('a.') == True, 'Test3'
#assert is_palindrome('aurora') == False, 'Test4'
#print("ОК")