#t = str(input().strip().split())
t = ["cat", "house", "hi"]
def all_eq(max:int, t:list[str])->list[str]:
    new_t = []
    for i in t:
        new_t.append(i.ljust(max,'_'))
    return new_t

_max = len(max(t,key=len))

_er = all_eq(_max,t)
print(_er)


#gpt
def all_eq(list_of_strings):
    # Находим максимальную длину строки в списке
    max_len = len(max(list_of_strings, key=len))
    
    # Создаём новый список, дополняя каждую строку справа символами '_'
    new_list = [s.ljust(max_len, '_') for s in list_of_strings]
    
    return new_list

# Пример использования
lst = ["cat", "house", "hi"]
result = all_eq(lst)
print(result)  # ['cat__', 'house', 'hi___']
