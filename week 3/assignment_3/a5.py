def gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

def divide_fractions(A, B, C, D):
    numerator = A * D - C * B 
    denominator = B * D
    g = gcd(numerator, denominator) 
    return numerator // g, denominator // g

# Пример
A, B, C, D = 2, 3, 1, 5   # 2/3 - 1/5
result = divide_fractions(A, B, C, D)
print(f"{result[0]}/{result[1]}")  # 7/15


n = int(input())
for i in range(1,int(n)+1):
    if(n%i==0):
        print(i, end=" ")