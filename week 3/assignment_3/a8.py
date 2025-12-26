#2
import random

m = int(input())
a = []
for i in range(0,m):
    a.append(random.randint(1,20))
print(a)

for i in range (0,int(m/2)):
    b = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = b
print(a)

#1

def check(num:int) -> bool:
    tmp = num
    while (tmp > 0):
        digit = int(tmp % 10)
        if(digit == 0 or num % digit !=0):
            return False
        tmp = tmp//10
    return True

n = 30
for i in range(1,n):
    if check(i):
        print(i,end=" ")