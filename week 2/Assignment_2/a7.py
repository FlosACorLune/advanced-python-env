test = "apple apple apple banana apple orange banana apple milk milk milk milk"
li = test.split(" ")
d = dict()

for prd in li:
    if prd in d:
        d[prd] += 1
    else:
        d[prd] = 1

new_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

for i,k in new_d.items():
    print(i,k)
