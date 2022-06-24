from itertools import combinations


def bananas(s) -> set:
    need = "banana"
    if len(s) < len(need):
        return set()
    res = set()                                         #Задаем пустой кортеж для return
    x = [i for i in range(len(s))]                      #Генерируем список индексов вводимой строки
    ind = list(combinations(x, len(x) - len(need)))     #Создаем список комбинаций индексов для замены на "-"
    list_s = []                                         #Создаем пустой список для складирование строк с "-"
    for row in ind:                                     #Проходимся по циклом по комбинациям индексов, заменяем на "-" в заданной строке
        s_edit = list(s)
        for j in row:
            s_edit[j] = "-"
        list_s.append(s_edit)                           #получаем список с уникальными строками с "-"
    for row in list_s:
        lst_ = "".join(row)                             #получаем строку из списка c "-"
        lst_clean = lst_.replace("-", "")               #получаем строку из списка без "-"
        if lst_clean == need:                           #если строка совпадает с "banana", то наполняем кортеж строками с "-"
            res.add(lst_)
    return res


s = "ban"
print(bananas(s))
