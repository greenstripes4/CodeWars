"""
Task
Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example
For n = 152, the output should be 52;

For n = 1001, the output should be 101.

Input/Output
[input] integer n

Constraints: 10 ≤ n ≤ 1000000.

[output] an integer
"""
def delete_digit2(n):
    n = str(n)
    lst = []
    for i in n:
        lst.append(i)
    for x in range(len(lst)):
        if lst[x] > lst[x+1]:
            if lst[x+2] <= lst[x+1]:
                del lst[x+1]
                string = ""
                for y in range(len(lst)):
                    string = string + lst[y]
                return int(string)
        else:
            del lst[x]
            string = ""
            for y in range(len(lst)):
                string = string + lst[y]
            return int(string)


def delete_digit(n):
    lst = []
    n=list(str(n))
    for i in range(len(n)):
        lst_to_append = n[:i] + n[i+1:]
        string = ""
        for x in lst_to_append:
            string = string + x
        lst.append(int(string))
    return max(lst)


print(delete_digit(152))
