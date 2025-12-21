if __name__ == '__main__':
    table = []
    table_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        table.append([name,score])
        table_score.append(score)
        
    table = sorted(table)
    print(table)
    
    second = sorted(set(table_score))[1]
    for i in range(len(table)):
        if(table[i][1]==second):
            print(table[i][0])

    
'''
37.21
37.21
37.2
41
39
'''