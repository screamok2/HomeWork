import Human
class Student(Human.Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if self.last_name == other.last_name:
            return True
        else:
            return False



