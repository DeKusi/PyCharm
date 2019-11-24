# 13
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def Display(self):
        print("First name :", self.firstname, "\nLast name :", self.lastname, "\nAge : ", self.age)


class Student(Person):
    def __init__(self, firstname, lastname, age, studentID, recordBook):
        Person.__init__(self, firstname, lastname, age)
        self.studentID = studentID
        self.recordBook = recordBook

    def Display(self):
        Person.Display(self)
        print ("Student ID : ", self.studentID, "\nRecord Book : ", self.recordBook, "\n")


# 14
class Professor(Person):
    def __init__(self, firstname, lastname, age, professorID, degree):
        Person.__init__(self, firstname, lastname, age)
        self.professorID = professorID
        self.degree = degree

    def Display(self):
        Person.Display(self)
        print ("ProfessorID : ", self.professorID, "\nDegree : ", self.degree, "\n")


Ethan = Student("Ethan", "Jones", 24, 2430, [3, 11, 4, 15])
Matthew = Student("Matthew", "Wilson", 21, 1234, [2, 13, 4, 15])
Kevin = Student("Kevin", "Moore", 23, 4563, [4, 12, 13, 1])
Ethan.Display()
Matthew.Display()
Kevin.Display()

Pol = Professor("Pol", "Taylor", 45, 7689, "Doctor of Philosophy")
Anthony = Professor("Anthony", "Brown", 52, 6590, "Doctor of Technical Science")
Justin = Professor("Justin", "Evans", 41, 9678, "Doctor of History")
Pol.Display()
Anthony.Display()
Justin.Display()
