# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
class Triangle(Shape):
    """Extend a shape Triangle from Shape"""
    def __init__(self,base,height):
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """Area of the triangle, overriding the main area()"""
        return 0.5*self.base*self.height
    def __str__(self):
        return "Triangle with base %0.1f and height %0.1f" % (self.base,self.height)
    def __eq__(self,other):
        """Compare type equality and value equality"""
        return type(other) == Triangle and self.base == other.base and self.height == other.height

## TO DO: Implement the `Triangle` class, which also extends `Shape`.
#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.


class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.shapes_list = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh not in self.shapes_list:
            #NB sh is of type(object created from) eg type(Circle)
            #We store the object
            self.shapes_list.append(sh)
    def __iter__(self):
        """ Return an iterator that allows you to iterate over
        the set of shapes, one shape at a time """
        # TO DO
        for item in self.shapes_list:
            yield item
    def __str__(self):
        all_shapes = ""
        self.shapes_list.sort()
        for shape in self.shapes_list:
            all_shapes += str(shape) + "\n"
        return all_shapes
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    max_area = max([x.area() for x in shapes])
    return tuple([c for c in shapes if c.area() == max_area])

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    shape_list = ShapeSet()
    with open(filename,'r') as f:
        for line in f:
            j = line.strip('\n').split(',')
            if j[0] == 'circle': shape_list.addShape(Circle(float(j[1])))
            elif j[0] == 'square': shape_list.addShape(Square(float(j[1])))
            elif j[0] == 'triangle': shape_list.addShape(Triangle(float(j[1]),float(j[2])))
    return shape_list
