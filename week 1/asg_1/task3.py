num = float(input()) #12.22

integer = int(num) #12
fraction = round((num-integer) * 100) # 0.22*100 = 22 round for rounding up otherwise output will be 
#22.120000000000065

swaped = fraction + integer/100
print(swaped)


# or 

num2 = float(input())
integer2, fraction2 = str(num2).split(".")
print(fraction2+"."+integer2)
