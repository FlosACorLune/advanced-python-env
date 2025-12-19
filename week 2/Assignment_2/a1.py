target1 = ">>-->"
target2 = "<--<<"

test = "<<<<>>--><--<<--<<>>>--><<<<<"

user = test#str(input("INPUT: "))
count = 0

for i in range(len(user)):
    if(user[i:i+5]==target1):
        count+=1
    if(user[i:i+5]==target2):
        count+=1
print(count)