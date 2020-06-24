from matrix import Matrix
from matrix import MatrixException

if __name__ == "__main__":
    filename: str = 'data.json'

    try:
        m = Matrix('date')
    except MatrixException as e:
        print(e)

    try:
        m = Matrix('data.csv')
    except MatrixException as e:
        print(e)

    try:
        m = Matrix(filename)
        print(m.average('something'))
    except MatrixException as e:
        print(e)

    try:
        m = Matrix(filename)
        print(m.average('name'))
    except MatrixException as e:
        print(e)

    try:
        m = Matrix(filename)
        print(m.average('average'))
        print(m.total('average'))
        print(m.min('average'))
        print(m.max('average'))
    except MatrixException as e:
        print(e)