# MIT600-pset9
### Problem 1 ###
We have implemented two different shape subclasses for you, namely Square and Circle. For each of these shapes, we are
interested in getting the area (note how the respective area methods override the area method of the Shape superclass),
checking for equality, and specifying a string representation of the object.

### Problem 2 ###
It may be handy to work with a set of shapes. In this problem we define a class, ShapeSet, which manages a set of shape
objects. Create a method, addShape, to add a shape to the set, with the stipulation that no two shapes in the set may be equal
(that is, when being compared with the == operator). The __iter__ method should return an iterator that allows you to iterate
over the set of shapes, one shape at a time. You may assume that the ShapeSet is not mutated while any iterator is active.

### Problem 3 ###
Now that we have a working representation of individual shapes and groups of shapes, we can utilize these in outside code. For
example, suppose we want to find the shape(s) with the largest area in a ShapeSet. This function will be outside of the classes
we’ve defined.
Write a function findLargest that returns a tuple containing all items in a ShapeSet with the largest area. 

### Problem 4 ###
Currently, to create a new ShapeSet, we are required to first create several individual shapes, then add them one by one to the
ShapeSet. If we want to use a large number of shapes or if we want to reuse the same shapes from one program to the next,
writing the code to create each can be tedious and redundant.
To solve this problem, we can store shape information in a file, then write a function to read the file line-by-line, creating a
ShapeSet with the information provided.
Write a function readShapesFromFile that will create and return a ShapeSet based on the information provided in the
given file. 
