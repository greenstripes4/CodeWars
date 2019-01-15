"""
Task
Given some sticks by an array V of positive integers, where V[i] represents the length of the sticks, find the number
of ways we can choose three of them to form a triangle.

Example
For V = [2, 3, 7, 4], the result should be 1.

There is only (2, 3, 4) can form a triangle.

For V = [5, 6, 7, 8], the result should be 4.

(5, 6, 7), (5, 6, 8), (5, 7, 8), (6, 7, 8)

Input/Output
[input] integer array V

stick lengths

3 <= V.length <= 100

0 < V[i] <=100

[output] an integer

number of ways we can choose 3 sticks to form a triangle.
"""
from itertools import combinations

def possibilities(arr,n):
    big_lst = []
    if n == 1:
        for i in arr:
            big_lst.append([i])
        return big_lst
    elif n == len(arr):
        return [arr]
    for y in range(len(arr) - (n-1)):
        a = [arr[y]]
        childList = possibilities(arr[(y+1):], n-1)
        for x in range(len(childList)):
            childList[x] = a + childList[x]
        big_lst = big_lst + childList
    return big_lst


def counting_triangles(V):
    count = 0
    for i in combinations(V,3):
        i = sorted(i)
        if i[0]+i[1] > i[2]:
            count += 1
    return count

print(counting_triangles([2, 3, 7, 4]))



