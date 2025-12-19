"""Content: Classes, Variables, Decorators."""

# from __future__ import annotations


# =================================================================================================
# Classes: Constructors runs first to init the object
class Gosu:
    """Class docstring."""

    MIN_SKILL = 1  # class var (won't be seen by the methods)
    MAX_SKILL = 10  # player can be iterated up to max skill
    skill = 3

    def __init__(self, skill=MIN_SKILL):  # constructor, 1st arg is always 'self'
        """If no skill is provided, default is 1."""
        # If no default was provided here, it would pick class var skill = 1"""
        self.name = "Alex"  # instance var (object specific)
        self.skill = skill  # starting skill
        self.max_skill = self.MAX_SKILL
        print(self.name + ", skill: " + str(self.skill))

    def __iter__(self):  # returns an object that has __next__ method
        """Docstring."""
        # self.skill = 6                # if we want to define a starting skill
        return self

    def __next__(self):  # method only for iter object
        """Docstring."""
        x = self.skill + 1  # store the current value
        if x == self.max_skill:  # bounds the constructor (common) skill to 10
            raise StopIteration
        return x

    def outer(self, a=0, d=0, s=0):  # a,d,s are keywords (order flexibile), defaults are 0
        """Docstring."""
        x = self.skill  # func var = outer local var (also among instance vars)
        attack = x + a
        defense = x + d
        speed = x + s
        return attack, defense, speed  # can return multiple vars/objects as a tuple

    def info(self):
        """Docstring."""
        print("Name: " + self.name + ", Attack: " + str(self.skill))

    def __del__(self):
        """Docstring."""
        class_name = self.__class__.__name__
        print(class_name + "destroyed")
        return None


# Usage: import Gosu --> lookup order: current dir > PYTHONPATH > default path
dir(Gosu)
help(Gosu)  # class summary
print(Gosu.__doc__)  # access class dosctring
print(Gosu.__init__.__doc__)  # access class.function dosctring

obj1 = Gosu  # notice no () used, constructor didn't run
print(Gosu.skill)  # = 3, class var access
print(obj1.skill)  # = 1, using default skill
print(obj1.name)  # = err, no default class var for name

obj2 = Gosu(5)  # now skill is supplied, constructor ran
print(Gosu.skill)  # = 1, supplied 5 is irrelevant
print([obj2.name, obj2.skill])  # = ['Alex', 5]
print(obj2.outer(a=3, d=2))  # = (5+2, 5+3) = (7, 8), accessing obj2 functions

obj2.info()  # Name: Alex, Attack: 5, gets the 5 from __init__
print(obj2.__next__)
print(obj2.__iter__)
print(obj2.__name__)  # err, no name attribute

hasattr(obj2, "age")  # no age attribute either
# setattr(obj2, "age", age)  # set it to 30
obj2.age = 30  # even better


# -------------------------------------------------------------------------------------------------
# Decorators:
class Calculate:
    """Showing different method types."""

    # @instancemethod:  decorator is not needed nor accepted
    def add(self, x, y):
        """Instance method: Decorator is not needed/accepted. Instance obj as the 1st param."""
        print(x + y)

    @classmethod  # decorator needed, no onject needed to call
    def sub(cls, x, y):
        """Must pass class obj as 1st param."""
        print(x - y)

    @staticmethod  # decorator not needed
    def mul(x, y):
        """No object needed for 1st param."""
        print(x * y)

    def div(self, x, y):
        """No decorator = static method."""
        print(x / y)


Calculate.add(2, 3)  # = err, need to create the instance first to access
cal1 = Calculate()
cal1.add(2, 3)  # = 5, now OK

Calculate.sub(2, 3)  # = 2 - 3 = -1, can directly
cal1.sub(2, 3)  # = -1, but works with instance too?

Calculate.mul(2, 3)  # = 2*3 = 6, instance
Calculate.div(2, 4)  # = 0.5
