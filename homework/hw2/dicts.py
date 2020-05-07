#Email: fadiatamny@gmail.com
# Students:
# Fadi Atamany, 206793275
# Annieli siegel, 302262720

# Write a function that calculates the average of a student given in a dict format.
# Write code to show how the function works.

# calculates the avg of a sutdent given a student in a dict format.


def avg(student: dict) -> float:
    numerator: int = 0
    denominator: int = 0
    marks: dict = student["marks"]

    for points, mark in marks.values():
        numerator += (points * mark)
        denominator += points

    if numerator == 0:
        return 0
    if denominator == 0:
        return -1

    return numerator / denominator


if __name__ == "__main__":
    student: dict = {
        'id': '666',
        'firstName': 'John',
        'lastName': 'Constantine',
        'marks': {
            'magic': (7, 100),
            'demonSummoning': (5, 95),
            'Curses': (3, 60),
            'Necromancy': (1, 20),
            'illusionCasting': (2, 100),
            'mindControl': (5, 100)
        }
    }

    studentAvg: float = avg(student)
    print('The average is {0:.3f}'.format(studentAvg)
          if studentAvg != -1 else 'MathError: Dividing by 0')
