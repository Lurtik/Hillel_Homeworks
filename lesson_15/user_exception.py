class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age} {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()} {self.record_book}'

class GroupOverflowError(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverflowError("Група не може містити більше 10 студентів")
        self.group.add(student)

    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        student = None
        for stu in self.group:
            if stu.last_name == last_name:
                student = stu
        return student

    def __str__(self):
        all_students = '\n'.join(str(stu) for stu in self.group)
        ...
        return f'Number:{self.number}\n {all_students} '