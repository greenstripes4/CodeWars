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
