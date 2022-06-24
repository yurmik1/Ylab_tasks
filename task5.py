def count_find_num(primesL, limit):
    primesL = set(primesL)
    numbers = []
    for i in range(limit+1):
        cur_primesL = set()
        cur_number = i
        d = 2
        while d * d <= i:
            if i % d == 0:
                cur_primesL.add(d)
                i //= d
            else:
                d += 1
        if i > 1:
            cur_primesL.add(i)
        if cur_primesL == primesL:
            numbers.append(cur_number)
    res = [len(numbers), max(numbers)] if numbers != [] else []
    return res



primesL = [2, 3]
limit = 200
print(count_find_num(primesL, limit))


#primesL = [2, 3]
#limit = 200
#assert count_find_num(primesL, limit) == [13, 192]

#primesL = [2, 5]
#limit = 200
#assert count_find_num(primesL, limit) == [8, 200]

#primesL = [2, 3, 5]
#limit = 500
#assert count_find_num(primesL, limit) == [12, 480]

#primesL = [2, 3, 5]
#limit = 1000
#assert count_find_num(primesL, limit) == [19, 960]

#primesL = [2, 3, 47]
#limit = 200
#assert count_find_num(primesL, limit) == []