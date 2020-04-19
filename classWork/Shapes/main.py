from circle import Circle
from rectangle import Rectangle


def main():
    shapes = [Rectangle(20, 10), Circle(5)]
    for shape in shapes:
        print("The area is {0:.3f}".format(shape.area()))


if __name__ == "__main__":
    main()
