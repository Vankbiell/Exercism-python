def equilateral(sides):
    for side in sides:
        if side <= 0:
            return False
    once = sides[0]
    for side in sides:
        if side != once:
            return False
    return True

def isosceles(sides):
    return sides


def scalene(sides):
    return sides
