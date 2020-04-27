# Write a simple program that keeps track of students and their test scores.
# If a student takes more than one test, keep track of the student's score average.

from collections import namedtuple
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Student():
    def __init__(self, name:str, score:int):
        self.name = name
        self.scores = []
        self.average = 0
        self.add_score(score)

    def add_score(self, score:int):
        self.scores.append(score)
        self.average = sum(self.scores)/len(self.scores)

    def __repr__(self):
        return str(self.__dict__)

    # def __str__(self):
    #     return f"{self.name} | {self.scores} | {self.average}"


class Ledger():
    def __init__(self):
        self.grades = {}

    def add(self, test:list):
        name = test[0]
        grade = test[1]
        if name in self.grades:
            student = self.grades[name]
            student.add_score(grade)
        else:
            self.grades[name] = Student(name, grade)

    def print_sorted(self):
        # Get all students in the ledger
        students = [student for student in self.grades.values()]
        # pp.pprint(students)
        students = sorted(students, key=lambda x: x.average, reverse=True)
        pp.pprint(students)


# bob = Student("Bob")
# bob.add_score(100)
# bob.add_score(50)
# print(bob)
##################

# Given:
t0 = ("Bob", 100)
t1 = ("Bob", 50)
t2 = ("Alice", 60)
t3 = ("Jane", 80)
tests = [t0, t1, t2, t3]

# Begin my solution:
ledger = Ledger()

for test in tests:
    ledger.add(test)

ledger.print_sorted()

# for key, val in ledger.grades.items():
#     print(val)
