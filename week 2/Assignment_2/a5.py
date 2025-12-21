n = '1234567890'
a ='ABCEHKMOPXTY'

test = 'P204BT'

t = str(input())

if(len(t)==6):     
    if t[0] in a and t[4] in a and t[5] in a and t[1] in n and t[2] in n and t[3] in n: 
        print("Yes")
    else:
        print("No")
else:
    print('No')