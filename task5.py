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



