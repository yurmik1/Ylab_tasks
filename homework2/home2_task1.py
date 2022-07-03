from itertools import permutations


def between_points(p1, p2):                                                 #расстояние между точками
    return ((points[p1][0] - points[p2][0]) ** 2 + (points[p1][1] - points[p2][1]) ** 2) ** 0.5


def calc_rout_matrix(cur_rout,j):                                           #расстояние между точками из матрицы
    return matrix[cur_rout[j]][cur_rout[j+1]]

#Можно использовать произвольное количество точек
n = 5               # Количество точек
point_1 = (0, 2)    # координаты первой точки
point_2 = (2, 5)    # координаты второй точки
point_3 = (5, 2)    # координаты 3-й точки
point_4 = (6, 6)    # координаты 4-й точки
point_5 = (8, 3)    # координаты 5-й точки


rout = (1, 2, 3, 4)                                                         # Путь по умолчанию
points = [globals()['point_' + str(i)] for i in range(1, n + 1)]            # list с координатами точек
len_rout = 0                                                                #длина пути
min_len_rout = float("inf")                                                 # минимальный путь по умолчанию. бесконечность
min_cur_rout = 0                                                            #минимальный маршрут

matrix = [[between_points(p1, p2) for p1 in range(n)] for p2 in range(n)]   # составление матрицы с расстояниями
routs = tuple(permutations(rout))                                           # составление различных путей

for i in routs:                                                             # перебираем пути
    cur_rout = (0,) + i + (0,)
    for j in range(n):
        len_rout += calc_rout_matrix(cur_rout, j)
    if len_rout < min_len_rout:
        min_len_rout = len_rout
        min_cur_rout = cur_rout
    len_rout = 0
print(f'{points[min_cur_rout[0]]}', end='')
for i in range(1, n):                                                      # вывод результата
    print(f' -> {points[min_cur_rout[i]]}[{calc_rout_matrix(min_cur_rout, i)}]', end='')
print(f' = {min_len_rout}')





