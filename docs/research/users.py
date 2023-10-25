from dataclasses import dataclass, replace
from enum import Enum


# Dataclasses are like java records or C structs
# https://docs.python.org/3/tutorial/classes.html#odds-and-ends
# https://docs.python.org/3/library/dataclasses.html
@dataclass
class Permissions:
    login: bool
    booking: bool

class User:
    # Constructor
    # https://docs.python.org/3/tutorial/classes.html#class-objects
    def __init__(self):
        # Declaration and instantiation of instance variables happens here and
        # NOT at the class level like in java.
        # https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
        self.name: str = "default_username"
        self.permissions = Permissions(
            login = True,
            booking = False,
        )
 
# For inheritance, Student is the derived class and User is the base class.
# Inheritance in python isn't 1:1 the same as Java's.
# https://docs.python.org/3/tutorial/classes.html#inheritance
class Student(User):
    def __init__(self, *args, **kwargs):
        # For extending the base class constructor one must call the base class
        # constructor first. Kind of like java's super() call at the start of an
        # overridden funtion but more ugly.
        # https://stackoverflow.com/questions/12701206/how-to-extend-python-class-init
        # https://stackoverflow.com/questions/904036/chain-calling-parent-initialisers-in-python
        super().__init__(*args, **kwargs)

class Faculty(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.permissions.booking = True

faculty = Faculty()
student = Student()
print("First Example")
print("Student = " + str(student.permissions))
print("Faculty = " + str(faculty.permissions))
print("")

# OOP edge case: 
# If a student works as faculty in the library then he can't book rooms like he
# might need to do for his job. A slightly contrived example but conveys how a
# users type might need to change after it is created. If there were mutally
# exclusive features to students and faculty then inheritance based on studnet
# type could get complicated. 

# Potential solution using one class.

DEFAULT_USER_PERMS = Permissions (
            login = True,
            booking = False,
        )

DEFAULT_FACULTY_PERMS = replace(DEFAULT_USER_PERMS, booking = True)


class UserTypes(Enum):
    STUDENT = 1
    FACULTY = 2
    VISITOR = 3

class GenericUser:
    def __init__(self):
        self.name: str = "default_username"
        self.type = UserTypes.VISITOR
        self.permissions = DEFAULT_USER_PERMS

    def set_faculty(self):
        self.type = UserTypes.FACULTY
        # Find a way to combined permissions rather than overwrite existing
        # permissions.
        self.permissions = DEFAULT_FACULTY_PERMS
     
student = GenericUser()
faculty = GenericUser()
faculty.set_faculty()
print("Second Example")
print("Student = " + str(student.permissions))
print("Faculty = " + str(faculty.permissions))
print("")
