test = "apple banana apple orange banana apple milk milk milk milk"
li = test.split(" ")
d = {}

for prd in li:
    if prd in d:
        d[prd] += 1
    else:
        d[prd] = 1

print(d.items())
this = {123,123,123,"124"}
#print(sorted(d.items()))