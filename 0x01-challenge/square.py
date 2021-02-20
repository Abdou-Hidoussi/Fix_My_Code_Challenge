#!/usr/bin/python3


class Square():
    """ Task 1 """
    def __init__(self, *args, **kwargs):
        """ Task 1 """
        self.width = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiterOfMySquare(self):
        """ Task 1 """
        return (self.width * 4)

    def __str__(self):
        """ Task 1 """
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":
    """ Task 1 """
    s = Square(width=10, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterOfMySquare())
