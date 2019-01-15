"""
Task
You have set an alarm for some of the week days.

Days of the week are encoded in binary representation like this:

0000001 - Sunday
0000010 - Monday
0000100 - Tuesday
0001000 - Wednesday
0010000 - Thursday
0100000 - Friday
1000000 - Saturday
For example, if your alarm is set only for Sunday and Friday, the representation will be 0100001.

Given the current day of the week, your task is to find the day of the week when alarm will ring next time.

Example
For currentDay = 4, availableWeekDays = 42, the result should be 6.

currentDay = 4 means the current Day is Wednesday
availableWeekDays = 42 convert to binary is "0101010"
So the next day is 6 (Friday)
Input/Output
[input] integer currentDay

The weekdays range from 1 to 7, 1 is Sunday and 7 is Saturday

[input] integer availableWeekDays

An integer. Days of the week are encoded in its binary representation.

[output] an integer

The next day available.
"""


def next_day_of_week(current_day, available_week_days):
    week_days = {1:"0000001",2:"0000010",3:"0000100",4:"0001000",5:"0010000",6:"0100000",7:"1000000"}
    available_week_days = str(bin(available_week_days))[2:]
    zeros_added = 7 - len(available_week_days)
    available_week_days = "0"*zeros_added + available_week_days
    current_day = week_days[current_day]
    for i in range(len(current_day)):
        if current_day[i] == "1":
            index = i
            break
    for x in range(len(available_week_days)*2,0,-1):
        if x <=14 and x>7:
            start = True
        else:
            start = False
        number = x%7-1
        if number == -1:
            number = 6
        if available_week_days[number] == "1":
            if start and number<index:
                next = number
                break
            elif start == False:
                next = number
                break
    for z in range(7):
        if week_days[z+1][next] == "1":
            return z+1


print(next_day_of_week(4,42))
