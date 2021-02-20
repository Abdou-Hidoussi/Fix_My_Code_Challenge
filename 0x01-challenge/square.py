#!/usr/bin/python3


class Square():
    """ Task 1 """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Task 1 """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiterOfMySquare(self):
        """ Task 1 """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Task 1 """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """ Task 1 """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterOfMySquare())
