import Student
import Human
import Group



st1 = Student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')


gr = Group.Group('PD1')
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


assert st1 == st1 , "Test3"
assert st1 != st2 , "Test4"