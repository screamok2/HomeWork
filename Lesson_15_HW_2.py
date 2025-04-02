class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        a1 = self.a * other.a
        b1 = self.b * other.b
        return Fraction(a1 , b1)

    def __add__(self, other): #"+"
        b2 = self.b * other.b
        a2 = b2//self.b * self.a  + b2//other.b*other.a
        return Fraction(a2 , b2)


    def __sub__(self, other): #"-"
        b2 = self.b * other.b
        a3 = b2 // self.b * self.a - b2 // other.b * other.a
        return Fraction(a3, b2)

    def __eq__(self, other):
        b2 = self.b * other.b
        if  b2//self.b * self.a == b2//other.b * other.a :
            return True
        else:
            False


    def __gt__(self, other):
        b2 = self.b * other.b
        if b2 // self.b * self.a > b2 // other.b * other.a:
            return True
        else:
            False

    def __lt__(self, other):
        b2 = self.b * other.b
        if b2 // self.b * self.a < b2 // other.b * other.a:
            return True
        else:
            return False

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
