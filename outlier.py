"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


def find_outlier(integers):
    dictionary = {"odd": 0, "even": 0}
    odd = None
    even = None
    for i in integers:
        if dictionary["even"] == 1 and dictionary["odd"] == 1:
            if i%2 == 0:
                return odd
            else:
                return even
        elif i%2 == 0 and dictionary["odd"] > 1:
            return i
        elif i%2 == 0 and dictionary["odd"] <= 1:
            dictionary["even"] += 1
            even = i
        elif i%2 == 1 and dictionary["even"] > 1:
            return i
        elif i%2 == 1 and dictionary["even"] <= 1:
            dictionary["odd"] += 1
            odd = i


print(find_outlier([2, 1, 2]))
