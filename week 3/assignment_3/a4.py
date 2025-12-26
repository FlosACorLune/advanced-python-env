def gcd(a, b):
    while b != 0:
        a, b = b, a % b # 10,12=12,10 ; 12,10 = 10,2 ; 10,2=2,0 ; 2,0 !
    return a

def divide_fractions(A, B, C, D):
    numerator = A * D #10
    denominator = B * C #12
    g = gcd(numerator, denominator) # 
    return numerator // g, denominator // g

# Пример
A, B, C, D = 2, 3, 4, 5   # 2/3 ÷ 4/5
result = divide_fractions(A, B, C, D)
print(f"{result[0]}/{result[1]}")  # 5/6



#(x/a)2 + (y/b)2 < R2 and points Р(р1, р2), F(f1, f1), L(l1,l2).

def count_points(points, a, b, R):
    count = 0
    for (x, y) in points:
        if (lambda x=x, y=y, a=a, b=b, R=R: (x**2)/(a**2) + (y**2)/(b**2) < R**2):
            count += 1
    return count


points = [(1, 2), (3, 3), (0, 0)]
a, b, R = 2, 2, 5
print(count_points(points, a, b, R))  # 3
