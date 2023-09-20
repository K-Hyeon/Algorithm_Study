"""
This module test the ABT/ Types(data structures) defined in Lab01 Molue
"""

from Lab01 import Functions, Complex, Point3D

def useFunctions():
    # getFactorial
    f1 = Functions()
    n = 5
    print("Factorial of {} is {}".format(n, f1.getFactorial((n))))

    # getTriples
    f1.getTriples(50)

    # drawTriangles
    f1.drawTriangles(5)

def useComplex():
    # Creating Complex objects
    z1 = Complex(1.5, 5.6)
    z2 = Complex(4.5, 3.7)

    # Using the __str__ method.
    print(z1)
    print(z2)

    # Using the __add__ method.
    z3 = z1+z2
    print('{} + {} = {}'.format(z1, z2, z3)) # result

    # Using the __mul__
    z4 = z1 * z2
    print('{} * {} = {}'.format(z1, z2, z4)) # result

    # Using the __abs__
    abs_z1 = abs(z1)
    abs_z2 = abs(z2)
    print('|z1|:', abs_z1) # result
    print('|z2|:', abs_z2) # result

    # Using the __eq__, __ne__, __gt__, and __le__ methods.
    z5 = Complex(1.5, 5.6)
    z6 = Complex(1.5, 5.6)

    # Comparing
    print("z5 == z6:", z1 == z6)  # z5 == z6: True
    print("z5 != z6:", z5 != z6)  # z5 != z6: False

    # Comparing
    print("z1 > z2:", z1 > z2)  # z1 > z2: False
    print("z1 <= z2:", z1 <= z2)  # z1 <= z2: True


def usePoin3D():
    # Creating Point3D objects.
    p1 = Point3D()
    p2 = Point3D(3.6, 2.3, 1.2)

    # Using the __str__ method.
    print(p1)
    print(p2)

    # Using the setCord method.
    p1.setCord(4.6, 6.7, 9.0)
    print("Updated p1:", p1)

    # Using the length method.
    print("Length of p1: {:.2f}".format(p1.length()))
    print("Length of p2:", p2.length())

    # Using the distance method.
    print("Distance between p1 and p2:", p1.distance(p2))

    # Using the __add__ method.
    print("p1 + p2:", p1 + p2)

    # Using the __sub__ method.
    print("p1 - p2:", p1 - p2)

    # Using the __eq__ method.
    print("p1 == p2:", p1 == p2)

    # Using the __gt__ and __le__ methods.
    print("p1 > p2:", p1 > p2)  # p1 > p2: True
    print("p1 <= p2:", p1 <= p2)  # p1 <= p2: False

def main():
    #useFunctions()
    #useComplex()
    usePoin3D()
    #pass

if __name__ == "__main__":
    main()