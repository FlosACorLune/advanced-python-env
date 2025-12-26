#1
a = int(input())
b = int(input())

print("square: ", a**a)
print("rectangle and parallegram: ", a*b)
print("circle: ", 3.14*(a**a))
print("triangle: ", 0.5*a*b)

#2
a  = list(map(int,input().split()))
b  = list(map(int,input().split()))
c  = list(map(int,input().split()))

print("Sum and mean of a", sum(a), sum(a)/len(a))
print("Sum and mean of b", sum(b), sum(b)/len(b))
print("Sum and mean of c", sum(c), sum(c)/len(c))
