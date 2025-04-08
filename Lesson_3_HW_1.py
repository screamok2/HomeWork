input_1 = int (input('input number 1 :'))
input_2 = input('input +,-,* or / :')
input_3 = int (input('input number 2:'))
if input_2 =="+" :
    print(f" {input_1}{input_2}{input_3} =",input_1 + input_3)
elif input_2 =="-" :
    print ( f" {input_1}{input_2}{input_3} =", input_1 - input_3)
elif input_2 =="*" :
    print ( f" {input_1}{input_2}{input_3} =", input_1 * input_3)
elif input_3 == 0:
    print("на 0 делити не можна")
elif input_3 != 0:
    if input_2 == "/":
        print ( f" {input_1}{input_2}{input_3} =",input_13 / input_3  )