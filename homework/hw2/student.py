class Student():
    def __init__(self, id, firstName, lastName, marks):
        self._id = id
        self._firstName = firstName
        self._lastName = lastName
        self._marks = marks

    def avg(self):
        numerator = 0
        denominator = 0

        for mark in self._marks:
            numerator += (self._marks[mark][0]*self._marks[mark][1])
            denominator += self._marks[mark][0]

        if denominator == 0:
            return -1

        return numerator/denominator


def studentAvg(student):
    return student.avg()


if __name__ == "__main__":
    marks = {
        'magic': (7, 100),
        'demonSummoning': (5, 95),
        'Curses': (3, 60),
        'Necromancy': (1, 20),
        'illusionCasting': (2, 100),
        'mindControl': (5, 100)
    }

    student = Student(666,'John','Constantine', marks)
    print("The average is {0:.3f}".format(studentAvg(student)))
