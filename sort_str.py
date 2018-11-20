def sort_by_length(arr):
    for i in range(len(arr)-1):
        for x in range(len(arr)-i-1):
            if len(arr[x]) > len(arr[x+1]):
                old_x=arr[x]
                arr[x]=arr[x+1]
                arr[x+1]=old_x
    return arr

tests = [
    [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
    [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
    [["short", "longer", "longest"], ["longer", "longest", "short"]],
    [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
    [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
    [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
]

for exp, inp in tests:
    print(sort_by_length(inp), exp)