class MyError(Exception):
    pass



class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group:

    def __init__(self, number, current_number_students=0 , max_students=10):
        self.number = number
        self.group = set()
        self.max_students = max_students
        self.current_number_students = current_number_students

    def add_student(self, student):
        self.group.add(student)
        self.current_number_students += 1
        if self.current_number_students > self.max_students:
            raise MyError("!!!!!!!!!!!!!!!TOO MUCH STUDENTS!!!!!!!!!!!")
        return self.current_number_students

    def delete_student(self, last_name):
        deleting_student = self.find_student(last_name)
        self.current_number_students -= 1
        if deleting_student in self.group:
            self.group.remove(deleting_student)

    def find_student(self, last_name):
        for  student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)

        return f'Number:{self.number}\n{all_students}\nNumber of students: {self.current_number_students}/10'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 35, 'Dave', 'Jonson', 'AN145')
st4 = Student('Female', 27, 'Anna', 'Scott', 'AN145')
st5 = Student('Male', 34, 'Piter', 'Parker', 'AN145')
st6 = Student('Female', 35, 'Natasha', 'Romanov', 'AN145')
st7 = Student('Male', 29, 'Steve', 'Rogers', 'AN145')
st8 = Student('Female', 35, 'Wanda', 'Marsimov', 'AN145')
st9 = Student('Male', 33, 'Garry', 'Ozborne', 'AN145')
st10 = Student('Female', 25, 'Linda', 'Gamilton', 'AN145')

st11 = Student('Female', 25, 'ANDY', 'Ttqe', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr)
if gr.current_number_students == 10:
    try:
        gr.add_student(st11)
    except MyError as e:
        print(e )



assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')

print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
