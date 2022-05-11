from person import Person
from student import Student

personType = input("Would you like to create a generic person (P) or student (S)? ")

if personType.lower() == "p":
    myPerson = Person()
elif personType.lower() == "s":
    myPerson = Student()

myPerson.readInputFromUser()
