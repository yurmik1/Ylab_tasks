from itertools import permutations


def between_points(p1, p2):                                                 #расстояние между точками
    return ((points[p1][0] - points[p2][0]) ** 2 + (points[p1][1] - points[p2][1]) ** 2) ** 0.5


def calc_rout_matrix(cur_rout, j):                                           #расстояние между точками из матрицы
    return matrix[cur_rout[j]][cur_rout[j+1]]

#Можно использовать произвольное количество точек, соблюдая формат названия переменных point
#n = 5             # Количество точек
#point_1 = (0, 2)    # координаты первой точки
#point_2 = (2, 5)    # координаты второй точки
#point_3 = (5, 2)    # координаты 3-й точки
#point_4 = (6, 6)    # координаты 4-й точки
#point_5 = (8, 3)    # координаты 5-й точки
#point_6 = (20.123, -100)
#point_7 = (9, 1)
#point_8 = (10, 5)
#point_9 = (6, 3)
#point_10 = (7, 4)



points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]        #Альтернативный ввод точек, можно удалять и добавлять вершины
n = len(points)                                                         # Количество вершин
rout = tuple([i for i in range(1, n)])                                      # Путь по умолчанию без учета нулевой точки

#points = [globals()['point_' + str(i)] for i in range(1, n + 1)]           # list с координатами точек
len_rout = 0                                                                #длина пути
min_len_rout = float("inf")                                                 # минимальный путь по умолчанию. бесконечность
min_rout = ()                                                                #минимальный маршрут
track = 0                                                                   # Длина траектории для отображения результата
matrix = [[between_points(p1, p2) for p1 in range(n)] for p2 in range(n)]   # составление матрицы с расстояниями
routs = tuple(permutations(rout))                                           # составление различных путей

for i in routs:                                                             # перебираем пути
    cur_rout = (0,) + i + (0,)
    for j in range(n):
        len_rout += calc_rout_matrix(cur_rout, j)                           # Рассчет каждого отрезка

    if len_rout < min_len_rout:                                             # Если текущий путь короче, чем предыдущие,
        min_len_rout = len_rout                                             # то сохраняем в переменную
        min_rout = cur_rout                                                 # и сохраняем текущую отпимальную траекторию
    len_rout = 0


print(f'{points[min_rout[0]]}', end='')

for i in range(1, n + 1):   # вывод результата
    track += calc_rout_matrix(min_rout, i - 1)
    print(f' -> {points[min_rout[i]]}[{track}]', end='')
print(f' = {min_len_rout}')





