"""
A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that
value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to
the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7
"""
def digital_root(n):
    if n<10:
        return n
    sum_of_digits=0
    while n != 0:
        sum_of_digits += n%10
        n=int(n/10)
    return digital_root(sum_of_digits)

print(digital_root(16))