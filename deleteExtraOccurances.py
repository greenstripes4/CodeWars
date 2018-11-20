def delete_nth(order,max_e):
    dictionary={}
    lst=[]
    for i in range(len(order)):
        if order[i] in dictionary:
            dictionary[order[i]] += 1
            if dictionary[order[i]] <= max_e:
                lst.append(order[i])
        else:
            dictionary[order[i]]=1
            lst.append(order[i])
    return lst

print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))

