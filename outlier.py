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
