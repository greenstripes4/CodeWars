"""
Task
Consider the following algorithm for constructing 26 strings S(1) .. S(26):

S(1) = "a";
For i in [2, 3, ..., 26]:
S(i) = S(i - 1) + character(i) + S(i - 1).
For example:

S(1) = "a"
S(2) = S(1) + "b" + S(1) = "a" + "b" + "a" = "aba"
S(3) = S(2) + "c" + S(2) = "aba" + "c" +"aba" = "abacaba"
...
S(26) = S(25) + "z" + S(25)
Finally, we got a long string S(26). Your task is to find the kth symbol (indexing from 1) in the string S(26). All
strings consist of lowercase letters only.

Input / Output
[input] integer k

1 ≤ k < 26

[output] a string(char in C#)

the kth symbol of S(26)
"""

lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]
previous_string = lst[0] + lst[1] + lst[0]
for i in range(2, 26):
    previous_string = previous_string + lst[i] + previous_string

def abacaba(k):
    return previous_string[k-1]

print(abacaba(5))
