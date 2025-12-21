ls, s = map(int, input().split())
t = str(input())

'''
3 1
abc

10 3
bbaabbbabb
'''


uniq = set()

tt = t+t

for i in range(ls-s+1):
    uniq.add(tt[i:i+s])

print(len(uniq))