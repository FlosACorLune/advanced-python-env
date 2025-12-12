#lucky number 
num = int(input())

num_size = len(str(num))

def luckynum():
    right = 0
    left = 0
    if num_size == 6:
        for i in range(0,int(num_size/2)):
            right+=int((num/10**i)%10)
            left+=int((num/10**(num_size-i-1))%10)
        #print(right,left)
        print("YES") if right==left else print("NO")
    else: 
        print("NO")

luckynum()