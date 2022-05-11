from person import Person

class Student(Person):

    def __init__(self, name="NA NA", DOB="0/0/0", school="NA",
                 GPA=0.0):
        super().__init__(name=name, DOB=DOB)
        self.school = school
        try:
            self.GPA = float(GPA)
        except ValueError:
            raise TypeError("GPA could not be cast to float")
        return

    def setSchool(self, school):
        self.school = school
        return

    def setGPA(self, GPA):
        try:
            self.GPA = float(GPA)
        except ValueError:
            raise TypeError("GPA could not be cast to float")
        return

    def getSchool(self):
        return self.school

    def getGPA(self):
        return self.GPA

    def readInputFromUser(self):
        super().readInputFromUser()
        school = input(f"Please enter {self.firstName}'s school: ")
        GPA = input(f"Please enter {self.firstName}'s GPA: ")
        self.setSchool(school)
        self.setGPA(GPA)
        return
