"""
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
"""


def delete_nth(order, max_e):
    dictionary = {}
    lst = []
    for i in range(len(order)):
        if order[i] in dictionary:
            dictionary[order[i]] += 1
            if dictionary[order[i]] <= max_e:
                lst.append(order[i])
        else:
            dictionary[order[i]] = 1
            lst.append(order[i])
    return lst


print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
