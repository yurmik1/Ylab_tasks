import math
from itertools import combinations_with_replacement


def count_find_num(primesL, limit):
    if math.prod(primesL) > limit:
        return []
    rates = ()
    n = ()

    for i in primesL:
        rate = 2
        while i <= limit:
            i = i**rate
            rate = rate + 1
        rates += (rate,)
    print(sum(rates))
    for i in range(len(primesL), sum(rates)+sum(rates) //2):
        n += tuple(combinations_with_replacement(primesL, i))
    n_edit = tuple(i for i in n if set(primesL) == set(i))
    numbers = tuple(math.prod(i) for i in n_edit if math.prod(i) <= limit)
    return [len(numbers), max(numbers)]

