"""
Task
Given a string str, reverse it omitting all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str

A string consists of lowercase latin letters, digits and symbols.

[output] a string
"""


def reverse_letter(string):
    return ''.join(e for e in string if e.isalpha())[::-1]



print(reverse_letter("ultr53o?n"))
