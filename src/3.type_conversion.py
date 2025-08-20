"""
Type Conversion
"""

import math
from random import random

X = input("Enter a number: ")

Y = round(float(X) * math.sqrt(math.pi), 2)

print(Y)

print(random())

print(type(X))

print(bool(X), str(Y), int(X), float(X))
