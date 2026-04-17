def isTriangle(sides):
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False    # not a Triangle, negative or 0 length side(s)
    if a + b > c and b + c > a and a + c > b:
        return True
    return False

def equilateral(sides):
    if not isTriangle(sides):
        return False
    a, b, c = sides
    return a == b and b == c

def isosceles(sides):
    if not isTriangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    if not isTriangle(sides):
        return False
    a, b, c = sides
    return a != b and b != c and a != c
