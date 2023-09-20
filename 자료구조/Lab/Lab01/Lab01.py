"""
This module contains the ADT for Lab01
"""

from math import sqrt, pi, pow
class Functions:
    def getFactorial(slef, n):
        if (n < 0): print("inaccurate input")
        elif (n ==0 or n==1): return 1
        else: return n * slef.getFactorial(n-1)

    def drawTriangles(self, lines):
        # n = 2*lines -1
        for line in range(1, lines+1):
            print(" " * (line-1), end= " ")
            print("*" * (2*lines+1 - 2*line))
        print()
        for line in range(lines,0,-1):
            print(" " * (line-1), end = " ")
            print("*" * (2*lines+1 - 2*line))

    def getTriples(self, bound):
        print("Triples within {}".format(bound))
        for a in range(1, bound):
            for b in range(1, bound):
                for c in range(1, bound):
                    if (a*a + b*b == c*c):
                        print("{}, {}, {}".format(a, b, c))



class Complex:
    def __init__(self, x=0.0, y=0.0):
        self.re = x
        self.im = y

    def re(self):
        return self.re
    def im(self):
        return self.im

    def __str__(self):
        return '({},{}i)'.format(self.re, self.im)

    def __repr__(self):
        return '(re={}, im={})'.format(self.re, self.im)

    def __add__(self, other):
        x = self.re + other.re
        y = self.im + other.im
        return Complex(x, y)

    def __mul__(self, other):
        x = (self.re * other.re) - (self.im * other.im)
        y = (self.im * other.re) + (self.re * other.im)
        return Complex(x, y)

    def __abs__(self):
        return sqrt((self.re * self.re) + (self.im * self.im))

    # equal
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    # not equal
    def __ne__(self, other):
        return not self.__eq__(other)

    # greater than
    def __gt__(self, other):
        return abs(self) > abs(other)

    # less than or equal
    def __le__(self, other):
        return abs(self) <= abs(other)

class Point3D:
    def __init__(self, x=0.0, y=10.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def __repr__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def setCord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

    def distance(self, p):
        d1 = (self.x - p.x) * (self.x - p.x)
        d2 = (self.y - p.y) * (self.y - p.y)
        d3= (self.z - p.z) * (self.z - p.z)
        return sqrt(d1+d2+d3)

    def translate(self, a, b, c):
        self.x += a
        self.y += b
        self.z += c

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)


    # equal
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    # greater than
    def __gt__(self, other):
        return  self.length() > other.length()

    # less than or equal
    def __le__(self, other):
        return self.length() <= other.length()