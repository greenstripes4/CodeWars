"""
Write

function combine()
that combines arrays by alternatingly taking elements passed to it.

E.g

combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
Arrays can have different lengths.
"""
def combine(*args):
    lst=[]
    for i in range(max([len(arr) for arr in args])):
        for x in range(len(args)):
            if i < len(args[x]):
                lst.append(args[x][i])
    return lst

print(combine(['a','b','c','d'], [1,2,3]))