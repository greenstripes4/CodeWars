"""
Task
An IP address contains four numbers(0-255) and separated by dots. It can be converted to a number by this way:

Given a string s represents a number or an IP address. Your task is to convert it to another representation(number to
IP address or IP address to number).

You can assume that all inputs are valid.

Example
Example IP address: 10.0.3.193

Convert each number to a 8-bit binary string (may needs to pad leading zeros to the left side):

10  -->  00001010
0   -->  00000000
3   -->  00000011
193 -->  11000001
Combine these four strings: 00001010 00000000 00000011 11000001 and then convert them to a decimal number: 167773121

Input/Output
[input] string s

A number or IP address in string format.

[output] a string

A converted number or IP address in string format.

Example
For s = "10.0.3.193", the output should be "167773121".

For s = "167969729", the output should be "10.3.3.193".
"""
def numberAndIPaddress2(s):
    if "." in s:
        lst=s.split(".")
        result=0
        for i in lst:
            result = (result << 8) + int(i)
        return str(result)
    else:
        input = int(s)
        results = ''
        for i in range(4):
            results = str(input % 256) + '.' + results
            input = input >> 8
        return results[:-1]

def numberAndIPaddress(s):
    if "." in s:
        lst=s.split(".")
        binary_list = []
        for i in lst:
            binary_number = str(bin(int(i)))[2:]
            padding = 8-len(binary_number)
            eight_bit = "0"*padding + binary_number
            binary_list.append(eight_bit)
        joined = ''.join(x for x in binary_list)
        return str(int(joined,2))
    else:
        binary_number = str(bin(int(s)))[2:]
        padding = 32 - len(binary_number)
        eight_bit = "0"*padding + binary_number
        lst = [eight_bit[x:x+8] for x in range(0, len(eight_bit), 8)]
        new_lst = []
        for i in lst:
            new_lst.append(str(int(i,2)))
        return '.'.join(z for z in new_lst)

print(numberAndIPaddress2("10.0.3.193"))
