if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks[query_name])
    test = student_marks.get(query_name)
    print(f"{sum(test)/len(scores):.2f}")
#до это было print(f"{sum(test)/3:.2f}") что поидее не должно было работать, но тест прошел: недочет автотестов
    
