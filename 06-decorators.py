from math import pi


class TypeChecker:
    required_type = object

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        assert isinstance(value, self.required_type), \
               f'Booooo! Expecting a {self.required_type.__name__}'
        instance.__dict__[self.name] = value


class IntType(TypeChecker):
    required_type = int


def type_check(**kwargs):
    def wrapper(cls):
        for var_name, checker_class in kwargs.items():
            setattr(cls, var_name, checker_class(var_name))
        return cls
    return wrapper


@type_check(x=IntType, y=IntType)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'A Point at {self.x}, {self.y}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class PointType(TypeChecker):
    required_type = Point


@type_check(center=PointType, radius=IntType)
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f'A Circle at {self.center.x}, {self.center.y} and ' + \
               f'radius {self.radius}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.center!r}, {self.radius!r})'


# Fewer lines of code!
# Mind-bending?
