def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

a = int(input())
b = int(input())

print("LCM: ", (a*b)/gcd(a,b))


def geron(x,y,z):
    s = (x+y+z)/2
    return pow(s*(s-x)*(s-y)*(s-z),0.5)

def area(a,b,c,d,p):
    a1 = geron(a,b,p)
    a2 = geron(c,d,p)
    return a1+a2

a,b,c,d,p = 5,6,7,8,9
print("AREA: ", area(a,b,c,d,p))