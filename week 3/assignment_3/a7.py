a,b,c,d = 5,6,7,8
rect = a*b
trian = c*d*0.5
area = rect + trian
print(area)


def decimal_to_octal(N):
    a=""
    while(N!=0):
        a += str(N%8)
        N=N//8
    return a
N = 104
s = decimal_to_octal(N)
s = s[::-1]
print(s.rjust(10,"0"))