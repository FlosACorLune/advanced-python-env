a = "abcabc"
b = "abc"

a_cycle = []
b_cycle = []

for i in range(len(a)):
    if len(a[i:i+len(b)]) ==3: 
        a_cycle.append(a[i:i+len(b)])
    
for i in range(len(b)):
    j=0
    b_cycle.append(b[i:i+len(b)])
print(b_cycle)