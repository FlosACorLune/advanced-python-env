text="nnnabc!n!nnn!"

max = 0
count = 0

for i in text:
    if i == 'n':
        count+=1
    else:
        if max < count:
            max = count
        count=0

new_text = text.replace('!','.')
print("the longest seq of n: ", max)
print(new_text)