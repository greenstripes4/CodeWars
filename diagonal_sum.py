def diagonal_sum(arr):
    for i, line in enumerate(arr):
        print(line,i)
    total=0
    for i in range(len(arr)):
        total=total+arr[i][i]
    return total

print(diagonal_sum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]))
