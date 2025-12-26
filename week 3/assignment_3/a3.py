a,b = int(input()),int(input())
d,c = int(input()),int(input())

A1 = (a**2 + b**2)**0.5
A2 = (d**2 + c**2)**0.5

if A1>A2:
    print("A1 is bigger")
elif A1<A2:
    print("A2 is bigger")
else: 
    print("They are equal")
    
    
g = list(map(str, input().split()))
j = []

for i in g:
    j.append(sorted(i))
print(j)