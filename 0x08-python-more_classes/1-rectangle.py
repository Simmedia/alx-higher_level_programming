#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if int(value):
            if value >= 0:
                self.__hieght = value
            else:
                print("height must be >= 0")
        else:
            print("height must be an interger")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if int(value):
            if value >= 0:
                self.__width = value
            else:
                print("width must be >= 0")
        else:
            print("width must be an integer")
