m = "9+x=1"
arr = []

number_set = '0123456789'
operation_set='+-'

for ch in m:
    arr.append(ch)

def parse():    
    if arr[0] in number_set:
        if arr[2] in number_set:
            print("Error you don't have 'x'")
        if arr[2] == 'x':
            if arr[1] in operation_set and arr[3]=='=' and arr[4] in number_set:
                match arr[1]:
                    case '-':
                        print(f"x = {int(arr[4])+int(arr[0])}")
                    case '+':
                        print(f"x = {int(arr[4])-int(arr[0])}")
            if arr[4] not in number_set:
                print('answer not number')
            if arr[3] != '=':
                print('doesnt have = ')
            if arr[1] not in operation_set:
                print("unknown operation")
    elif arr[0] == 'x':
        if arr[2] in number_set:
            if arr[1] in operation_set and arr[3]=='=' and arr[4] in number_set:
                match arr[1]:
                    case '-':
                        print(f"x = {int(arr[4])+int(arr[2])}")
                    case '+':
                        print(f"x = {int(arr[4])-int(arr[2])}")
            if arr[4] not in number_set:
                print('answer not number')
            if arr[3] != '=':
                print('doesnt have = ')
            if arr[1] not in operation_set:
                print("unknown operation")
        if arr[2] == 'x':
            print("Error you don't have 'number'")
    else:
        print('you dont have neigher number nor x')

(parse())
    
    
print(arr)



# chatpgt
m = "9+x=1"

a = m[0]
op = m[1]
b = m[2]
eq = m[3]
c = m[4]

numbers = '0123456789'

# Convert known values
if a != 'x':
    a = int(a)
if b != 'x':
    b = int(b)
if c != 'x':
    c = int(c)

if eq != '=' or op not in '+-':
    print("Invalid equation")
else:
    if a == 'x':
        if op == '+':
            x = c - b
        else:
            x = c + b

    elif b == 'x':
        if op == '+':
            x = c - a
        else:
            x = a - c

    else:  # c == 'x'
        if op == '+':
            x = a + b
        else:
            x = a - b

    print(x)
