'''
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string
with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
'''
def dashatize(num):
    if "-" in str(num):
        num=str(num).replace("-","")
    else:
        num=str(num)
    lst=list(num)
    dashed=""
    for i in range(len(lst)):
        if i+1 == len(lst):
            if int(lst[i])%2 == 1:
                dashed += "-" + lst[i]
        else:
            if int(lst[i]) % 2 == 1:
                dashed += "-" + lst[i] + "-"
    return dashed


print(dashatize(274))
print(dashatize(5311))
print(dashatize(-28369))
