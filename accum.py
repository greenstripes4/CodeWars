def accum(s):
    string = ""
    index = 0
    for c in s:
        if index > 0:
            string += '-'
        string += c.upper()
        if index >= 1:
            string += c.lower() * index
        index += 1
    return string


print(accum("RqaEzty"))
