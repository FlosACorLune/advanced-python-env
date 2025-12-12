word = str(input("Enter a word: "))
num = int(input("Enter a number: "))

for k in range(0,len(word)):
    for i in range(0,num):
        print(word[k],end="")
    print()

#or
print("Method 2")
for i in word:
    print(i * num)