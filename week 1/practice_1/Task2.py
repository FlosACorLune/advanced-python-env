print("Enter 1st number")
a = int(input())
print("Enter 2nd number")
b = int(input())
print("Enter operation")
d = str(input())

match d:
    case '-':
        print(a-b)
    case '+':
        print(a+b)
    case '*':
        print(a*b)
    case '/':
        if a!=0:
            print(a/b)
        else:
            print("Cannot divide 0")
    case _:
        print("Incorrect operation input")