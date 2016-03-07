class Rectangle(object):
    """Common base class for rectangles"""

    def __init__(self, width, length):
      self.width = width
      self.length = length

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def equal_to(self, rectangle_other):
        return self.get_area() == rectangle_other.get_area()