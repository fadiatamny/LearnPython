#Email: fadiatamny@gmail.com
# Students:
# Fadi Atamany, 206793275
# Annieli siegel, 302262720

# Build a class that defines a student and it contains a method to calculate the average of a student.
# Write code to show how the function works.


class Student():
    def __init__(self, id: int, firstName: str, lastName: str, marks: dict) -> None:
        self.__id: int = id
        self.__firstName: str = firstName
        self.__lastName: str = lastName
        self.__marks: dict = marks

    # function that calculates the average of a student
    def avg(self) -> float:
        numerator: int = 0
        denominator: int = 0

        for points, mark in self.__marks.values():
            numerator += (points * mark)
            denominator += points

        if numerator == 0:
            return 0
        if denominator == 0:
            return -1

        return numerator / denominator


if __name__ == "__main__":
    marks: dict = {
        'magic': (7, 100),
        'demonSummoning': (5, 95),
        'Curses': (3, 60),
        'Necromancy': (1, 20),
        'illusionCasting': (2, 100),
        'mindControl': (5, 100)
    }

    student: Student = Student(666, 'John', 'Constantine', marks)
    studentAvg: float = student.avg()
    print('The average is {0:.3f}'.format(studentAvg)
          if studentAvg != -1 else 'MathError: Dividing by 0')
