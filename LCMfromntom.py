"""
Task
Your task is to find the smallest number which is evenly divided by all numbers between m and n (both inclusive).

Example
For m = 1, n = 2, the output should be 2.

For m = 2, n = 3, the output should be 6.

For m = 3, n = 2, the output should be 6 too.

For m = 1, n = 10, the output should be 2520.

Input/Output
[input] integer m

1 ≤ m ≤ 25

[input] integer n

1 ≤ n ≤ 25

[output] an integer
"""
def modified_euclids_algorithm(x,y):
    original_x = x
    original_y = y
    gcf = x%y
    while gcf != 0:
        x=y
        y=gcf
        gcf=x%y
    return int(y*(original_y/y)*(original_x/y))


def mn_lcm(m,n):
    if m == n:
        return m
    maximum = max(m,n)
    minimum = min(m,n)
    lcm=modified_euclids_algorithm(minimum,minimum+1)
    while minimum != maximum:
        lcm = modified_euclids_algorithm(lcm,minimum+1)
        minimum += 1
    return lcm

print(mn_lcm(1,10))
