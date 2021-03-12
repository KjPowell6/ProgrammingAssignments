######################################################################################################################
# Name: Kyle Powell
# Date: 3-12-21
# Description: 2D Points
######################################################################################################################

# the 2D point class
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

# The following four functions are the getter and setter functions for the x and y values.
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

# The dist function takes in two points, self and other. The x and y values of each Point is plugged in to the distance
# formula which is assigned to the variable distance. Distance is then returned.
    def dist(self, other):
        distance = ((other.x - self.x) **2 + (other.y - self.y)**2)**0.5
        return distance

# The midpt function takes in two points, and assigns the average of the x values of each point to the
# variable val_x. It does the same for the y values and stores it in the variable val_y. The function then
# returns these values as the parameters for the Point class.
    def midpt(self, other):
        val_x = (self.x + other.x)/2
        val_y = (self.y + other.y)/2
        return Point(val_x, val_y)

# The magic method formats the function to print out the float values as an ordered pair.
    def __str__(self):
        return "({},{})".format(float(self.x), float(self.y))


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print("p1:", p1)
print("p2:", p2)
print("p3:", p3)
# calculate and display some distances
print("distance from p1 to p2:", p1.dist(p2))
print("distance from p2 to p3:", p2.dist(p3))
print("distance from p1 to p3:", p1.dist(p3))
# calculate and display some midpoints
print("midpt of p1 and p2:", p1.midpt(p2))
print("midpt of p2 and p3:", p2.midpt(p3))
print("midpt of p1 and p3:", p1.midpt(p3))
# just a few more things...
p4 = p1.midpt(p3)
print("p4:", p4)
print("distance from p4 to p1:", p4.dist(p1))
