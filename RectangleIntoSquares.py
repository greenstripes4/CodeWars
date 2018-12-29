"""
Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
You will return an array or a string (depending on the language; Shell bash and Fortran return a string) with the size of each of the squares.
"""
def sqInRect(lng, wdth, is_start=True):
    if lng == wdth:
        if is_start:
            return None
        else:
            return [lng]
    return [min(lng, wdth)] + sqInRect(max(lng, wdth) - min(lng, wdth), min(lng, wdth), is_start=False)

print(sqInRect(1,4))
print(sqInRect(3,5))

