#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

'''
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''


if __name__ == '__main__':
    nums = []
    N = int(input()) #4 commands
    for v in range(N):
        cmd, *line = input().split()
        line = list(map(int,line))
        
        match cmd:
            case 'print':
                print(nums)
            case 'append':
                nums.append(line[0])
            case 'pop':
                nums.pop()
            case 'remove':
                nums.remove(line[0])
            case 'reverse':
                nums.reverse()
            case 'insert':
                nums.insert(line[0], line[1])
            case 'sort':
                nums.sort()
                