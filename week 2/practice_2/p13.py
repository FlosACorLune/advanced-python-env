text = "ab(cd(ef)g)hij(k(lm)n)o(pq)r(st(u)v)wx(yz)"

level = 0
current = ''

for ch in text:
    if ch == '(':
        if level > 0:
            current += ch
        level += 1

    elif ch == ')':
        level -= 1
        if level > 0:
            current += ch
        else:
            print(current)
            current = ""

    else:
        if level > 0:
            current += ch