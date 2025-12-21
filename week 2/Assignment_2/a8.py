a1 = str(input())
a2 = str(input())

d = {}
        
for l1,l2 in zip(a1,a2):
    d[l1] = d.get(l1, 0) + 1
    d[l2] = d.get(l2, 0) - 1
    
if all(v == 0 for v in d.values()):
    print("YES")
else:
    print("NO")