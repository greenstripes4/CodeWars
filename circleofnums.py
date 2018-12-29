"""
Task
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two
neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).

Given n and firstNumber/first_number, find the number which is written in the radially opposite position to firstNumber.

Example
For n = 10 and firstNumber = 2, the output should be

circleOfNumbers n firstNumber == 7


Input/Output
[input] integer n

A positive even integer.

Constraints: 4 ≤ n ≤ 1000.

[input] integer firstNumber/first_number

Constraints: 0 ≤ firstNumber ≤ n - 1

[output] an integer
"""

def circle_of_numbers(n, fst):
    return int((fst + n/2) % n)

print(circle_of_numbers(6,3))