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