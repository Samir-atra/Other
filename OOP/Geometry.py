import sys
import math


class Geometry:
    def __init__(self, side):
        self.side = side

    @property
    def triangle(self):
        beedoo = 2 * int(self.side)
        if int(self.side) % 2 == 0:
            print("it's not pointy, input an odd number")
            for i in range(beedoo):
                if i % 2 == 1:
                    continue
                else:
                    print(str("#" * i).center(beedoo, " "))
        elif int(self.side) % 2 == 1:
            for i in range(beedoo + 1):
                if i % 2 == 0:
                    continue
                else:
                    print(str("#" * i).center(beedoo, " "))

    @property
    def square(self):
        for i in range(int(self.side)):
            print("# " * int(self.side))

    @property
    def rectangle(self):
        for i in range(math.floor(int(self.side) / 2)):
            print("# " * int(self.side))

    # @property
    # def trapezoid(self):
    #     for i in range # another equation


def main():
    shape = sys.argv[1]
    inp = input("type a side length: ")
    tri = Geometry(inp)
    getattr(tri, shape)


if __name__ == "__main__":
    main()
