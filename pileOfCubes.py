"""
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3,
the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to
build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer
n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
"""
def find_nb(m, sums=0):
    if m == 0:
        return 0
    elif m<0:
        return -1
    sums=sums+1
    recursion=find_nb(m-(sums)*(sums)*(sums), sums=sums)
    if recursion == -1:
        return -1
    return 1 + recursion

def find_nb_2(m):
    times=0
    number=1
    while m>0:
        times += 1
        m=m-pow(number,3)
        number=number+1
    if m == 0:
        return times
    if m < 0:
        return -1


print(find_nb_2(4183059834009))
#print(find_nb(1))
#print(find_nb(9))