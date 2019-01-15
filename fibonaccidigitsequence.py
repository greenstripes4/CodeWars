"""
Task
You are given three non negative integers a, b and n, and making an infinite sequence just like fibonacci sequence, use
the following rules:

step1: use ab as the initial sequence.

step2: calculate the sum of the last two digits of the sequence, and append it to the end of sequence.

repeat step2

Your task is to complete function find. Return nth digit(0-based) of the sequence.

Note
0 <= a,b <= 9, 0 <= n <= 10^10

16 fixed test cases

100 random test cases, testing for correctness of solution

100 random test  cases, testing for performance of code

All inputs are valid.

Pay attention to code performance.

Example
For a = 7, b = 8 and n = 9, the output should be 5.

Because:

sequence is:
78 -> 7815 -> 78156 -> 7815611
   -> 78156112 -> 781561123 -> 7815611235 -> ....
the 9th digit of the sequence is 5
For a = 0, b = 0 and n = 100000000, the output should be 0.

Obviously, all the digits in this sequence are 0.
"""


def find(a,b,n):
    if a == 0 and b == 0:
        return 0
    string = str(a)+str(b)
    while len(string) <= n:
        total = int(string[-1]) + int(string[-2])
        string = string + str(total)
    return int(string[n])


def find2(a,b,n):
    if a == 0 and b == 0:
        return 0
    n -= 2
    while n>=0:
        if a==1:
            if b==1:
                n = n % 10
            elif b==4:
                n = n % 4
        temp = a+b
        if temp < 10:
            a = b
            b = temp
            n -= 1
        else:
            a = temp // 10
            b = temp % 10
            n -= 2
    if n == -1:
        return b
    else:
        return a

print(find2(7,8,9))
"""
101123581347 11
1123581347 11
1235813471 12
1347112358 13
1459 14
1561123581347 11
1671347112358 13
1781561123581347 11
1891781561123581347 11
"""


'''
101123581347112358
1123581347112358
123581347112358
13471123581347112358
1459145914591459145914591459
15611235813
167134711235
178156112358134
189178156112358
'''