import math

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def set_width(self,width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        pic = ""
        for i in range(self.height):
            pic += self.width * "*" + '\n'
        return pic
    def get_amount_inside(self,shape):
        divHeight = self.height / shape.height
        if divHeight < 1:
            return 0
        divWidth = self.width / shape.width
        if divWidth < 1:
            return 0
        return max(math.floor(divWidth),math.floor(divHeight)) * min(math.floor(divWidth),math.floor(divHeight))
    def __repr__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" +  str(self.height) + ")"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def set_side(self,something):
        self.width = something
        self.height = something
    def set_width(self,something):
        self.width = something
        self.height = something
    def set_height(self,something):
        self.width = something
        self.height = something
    def __repr__(self):
        return "Square(side=" + str(self.height) + ")"