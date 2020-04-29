#Email: fadiatamny@gmail.com
# Students:
# Fadi Atamany, 206793275
# Annieli siegel, 302262720

# Write a function that calculates the average of a student given in a dict format.
# Write code to show how the function works.

# calculates the avg of a sutdent given a student in a dict format.


def avg(student):
    numerator = 0
    denominator = 0

    marks = student["marks"]

    for mark in marks:
        numerator += (marks[mark][0]*marks[mark][1])
        denominator += marks[mark][0]

    if denominator == 0:
        return -1

    return numerator/denominator


if __name__ == "__main__":
    student = {
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
    print("The average is {0:.3f}".format(avg(student)))
