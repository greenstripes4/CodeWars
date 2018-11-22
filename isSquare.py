"""
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.
"""
import math
def is_square(n):
    if n<0:
        return False
    value=math.sqrt(n)
    if math.sqrt(n)==int(math.sqrt(n)):
        value=int(math.sqrt(n))
    if type(value) is int:
        return True
    else:
        return False
print(is_square(16))
