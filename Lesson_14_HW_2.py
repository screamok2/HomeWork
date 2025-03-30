import Student
import Human


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
            raise ValueError("TOO MUCH STUDENTS")
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

st1 = Student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')


gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)


print(gr)


assert gr.find_student('Jobs') == st1, 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student.Student) is True, 'Метод поиска должен возвращать экземпляр'
assert gr.find_student('Jobs') == st1

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
