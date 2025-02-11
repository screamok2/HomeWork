number = int(input('input number'))
number1 = number % 10
number2 = number % 100 // 10
number3 = number % 1000 // 100
number4 = number % 10000 // 1000
number5 = number // 10000
print(f"{number1}{number2}{number3}{number4}{number5}")