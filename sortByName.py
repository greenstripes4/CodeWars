"""
Hey You !
Sort these integers for me ...

By name ...

Do it now !

Input
Range is 0-999

There may be duplicates

The array may be empty
"""
def posInLine(hList,hPete):
    low=0
    high=len(hList)-1
    while low!=high:
        mid = int((low+high)/2)
        if hList[mid] > hPete:
            low = mid+1
        elif hList[mid] < hPete:
            high = mid-1
    return high

def sort_by_name(arr):
    numbers = {0: 4, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6}
    sorted_list = []
    for i in arr:
        if i<13:
            position = posInLine(sorted_list, digits[i])
            sorted_list[position] = i
        elif i>=13 and i<20:

