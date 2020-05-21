# Email: fadiatamny@gmail.com
# Students:
# Fadi Atamany, 206793275
# Annieli siegel, 302262720

# target : write a class that represents a triangle
# if the recieved lengths do not create a triangle throw a TriangleException


class TriangleException(Exception):
    def __init__(self, message: str):
        super().__init__(self)
        self._message = message

    def __str__(self) -> str:
        return self._message


class Triangle:
    def __init__(self, a: float, b: float, c: float):

        if min(a, b, c) < 0:
            raise TriangleException('Sides of a triangle cannot be negative')
        if min(a, b, c) == 0:
            raise TriangleException('Sides of a triangle cannot be 0')
        if 2 * max(a, b, c) >= a + b + c:
            raise TriangleException('The given lengths cannot form a correct triangle')

        self._a = a
        self._b = b
        self._c = c


try:
    Triangle(1, 2, 2)
except TriangleException as e:
    print('Error Occured: ', e)
