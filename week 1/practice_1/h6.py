#To check if a year is a leap year, it must be divisible by 4 and not divisible by 100 or divisible by 400.

def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))