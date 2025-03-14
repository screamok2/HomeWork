def pow (x):
   return x**2

def some_gen( begin, end, func):
    for i in range (begin, end):
       i = func(i)
       yield i

gen = some_gen(1, 10, pow )

for number in gen:
    print(number)
