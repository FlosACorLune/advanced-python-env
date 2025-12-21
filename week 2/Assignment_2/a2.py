a = "abcabc"
b = "abc"

a_cycle = []
b_cycle = []

for i in range(len(a)):
    if len(a[i:i+len(b)]) == 3: 
        a_cycle.append(a[i:i+len(b)])
    
for i in range(len(b)):
    if len(b[i:i+len(b)]) <= 2:
        b_cycle.append(b[i:i+len(b)]+b[0:i])
    else:
        b_cycle.append(b[i:i+len(b)]) 

count = 0
for b in b_cycle:
    for a in a_cycle:
        if(b in a):
            count+=1
print(count)
print(a_cycle)
print(b_cycle)


#### chatgpt 
a = input().strip()
b = input().strip()

n = len(a)
m = len(b)

# Generate all cyclic shifts of b
bb = b + b
cyclic_shifts = set(bb[i:i + m] for i in range(m))

# Count substrings of a that are cyclic shifts of b
count = 0
for i in range(n - m + 1):
    if a[i:i + m] in cyclic_shifts:
        count += 1

print(count)
