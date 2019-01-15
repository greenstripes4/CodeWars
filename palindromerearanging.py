"""
Task
Given a string s, find out if its characters can be rearranged to form a palindrome.

Example
For s = "aabb", the output should be true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output
[input] string s

A string consisting of lowercase English letters.

Constraints:

4 ≤ inputString.length ≤ 50.

[output] a boolean value

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""

from collections import Counter

def palindrome_rearranging2(s):
    return sum(n % 2 for n in Counter(s).values()) <= 1

def palindrome_rearranging(s):
    if len(s)%2 == 0:
        for i in set(s):
            if s.count(i)%2 != 0:
                return False
        return True
    else:
        count = 0
        for i in set(s):
            if s.count(i)%2 != 0:
                count += 1
        if count > 1:
            return False
        return True


print(palindrome_rearranging2("zyzzzzzz"))