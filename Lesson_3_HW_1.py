input_1 = int (input('input number 1 :'))
input_2 = input('input number +,-,* or / :')
input_3 = int (input('input number 2:'))
if input_2 =="+" :
    print(f" {input_1}{input_2}{input_3} ="), print( input_1 + input_3 )
if input_2 =="-" :
    print ( f" {input_1}{input_2}{input_3} =" ),print( input_1 - input_3 )
if input_2 =="*" :
    print ( f" {input_1}{input_2}{input_3} =" ),print( input_1 * input_3 )
if input_3 == 0:
    print("на 0 делити не можна")
if input_3 != 0:
    if input_2 == "/":
        print ( f" {input_1}{input_2}{input_3} =" ), print (input_1 / input_3)