class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        '''Добавляет оценку лектору по курсу'''
        if (grade > 0 and grade <= 10) and (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
            and course in lecturer.courses_attached and course in lecturer.courses_attached):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
        else:
            return "Ошибка, введены некорректные данные"

    def avg_rating(self):
        '''Выводит среднюю оценку по всем домашним заданиям студента'''
        evaluations = []
        for value in self.grades.values():
            evaluations.extend(value)
        if len(evaluations) !=0:
            return sum(evaluations) / len(evaluations)
        else:
            return 0

    def __eq__(self, student):
        return (self.avg_rating() == student.avg_rating())

    def __ne__(self, student):
        return (self.avg_rating() != student.avg_rating())

    def __lt__(self, student):
        return (self.avg_rating() < student.avg_rating())

    def __gt__(self, student):
        return (self.avg_rating() > student.avg_rating())

    def __le__(self, student):
        return (self.avg_rating() <= student.avg_rating())

    def __ge__(self, student):
        return (self.avg_rating() >= student.avg_rating())

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.avg_rating():.2f}\n"
                f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {", ".join(self.finished_courses)}")
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_rating(self):
        '''Выводит среднюю оценку по всем оценкам от студентов за лекции'''
        evaluations = []
        for value in self.grades.values():
            evaluations.extend(value)
        if len(evaluations) != 0:
            return sum(evaluations) / len(evaluations)
        else:
            return 0

    def __eq__(self, lecturer):
        return (self.avg_rating() == lecturer.avg_rating())

    def __ne__(self, lecturer):
        return (self.avg_rating() != lecturer.avg_rating())

    def __lt__(self, lecturer):
        return (self.avg_rating() < lecturer.avg_rating())

    def __gt__(self, lecturer):
        return (self.avg_rating() > lecturer.avg_rating())

    def __le__(self, lecturer):
        return (self.avg_rating() <= lecturer.avg_rating())

    def __ge__(self, lecturer):
        return (self.avg_rating() >= lecturer.avg_rating())

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rating():.2f}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        '''Добавляет оценку студенту по курсу в процессе обучения'''
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def student_list_avg_of_course(student_list, course):
    '''Возвращает среднюю оценку по курсу среди всех студентов'''
    rate_list = []
    for student in student_list:
        if course not in student.grades:
            continue
        rate_list.extend(student.grades[course])
    if len(rate_list)<=0:
        print("Оценок среди студентов по данному курсу нет")
    else:
        avg_of_course = sum(rate_list) / len(rate_list)
        print(f"Средняя оценка по курсу среди всех студентов равна: {avg_of_course:.2f}")

def lecturer_list_avg_of_course(lecturer_list, course):
    '''Возвращает среднюю оценку по курсу среди всех лекторов'''
    rate_list = []
    for lecturer in lecturer_list:
        if course not in lecturer.grades:
            continue
        rate_list.extend(lecturer.grades[course])
    if len(rate_list)<=0:
        print("Оценок среди лекторов по данному курсу нет")
    else:
        avg_of_course = sum(rate_list) / len(rate_list)
        print(f"Средняя оценка по курсу среди всех лекторов равна: {avg_of_course:.2f}")


student1 = Student("Ivan", "Ivanov", "male")
student1.finished_courses += ["C++"]
student1.courses_in_progress += ["Java", "C#", "Python"]
student2 = Student("Petr", "Petrov", "male")
student2.finished_courses += ["Java"]
student2.courses_in_progress += ["Delphi", "C++", "Python"]

lecturer1 = Lecturer("Alexandra", "Alexandrova")
lecturer1.courses_attached += ["Python", "Java", "Delphi"]
lecturer2 = Lecturer("Stepan", "Stepanov")
lecturer2.courses_attached += ["C#", "Delphi", "C++"]

reviewer1 = Reviewer("Dmitriy", "Dmitriev")
reviewer2 = Reviewer("Egor", "Egorov")

student1.rate_lecturer(lecturer2, "C#", 10)
student1.rate_lecturer(lecturer1, "Java", 10)
student2.rate_lecturer(lecturer1, "Delphi", 10)
student2.rate_lecturer(lecturer2, "Delphi", 7)
student2.rate_lecturer(lecturer2, "C++", 9)
student2.rate_lecturer(lecturer1, "Python", 8)

reviewer1.rate_hw(student1, "Java", 4)
reviewer1.rate_hw(student1, "Python", 4)
reviewer2.rate_hw(student1, "Java", 5)
reviewer2.rate_hw(student1, "C#", 4)
reviewer2.rate_hw(student1, "C#", 3)
reviewer1.rate_hw(student2, "Delphi", 5)
reviewer2.rate_hw(student2, "C++", 4)
reviewer2.rate_hw(student2, "Python", 3)
reviewer1.rate_hw(student2, "Python", 3)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(student1 == student2)
print(student1 != student2)
print(student1 < student2)
print(student1 > student2)
print(student1 <= student2)
print(student1 >= student2)

print(lecturer1 == lecturer2)
print(lecturer1 != lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 <= lecturer2)
print(lecturer1 >= lecturer2)



student_list = [student1, student2]
student_list_avg_of_course(student_list, "C++")

lecturer_list = [lecturer1, lecturer2]
lecturer_list_avg_of_course(lecturer_list, "Delphi")

