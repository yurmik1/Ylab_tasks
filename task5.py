def count_find_num(primesL, limit):
    primesL = set(primesL)
    numbers = set()
    for i in range(2, limit + 1):
        cur_primes_l = set()
        cur_number = i
        for j in primesL:

            while i % j == 0:
                cur_primes_l.add(j)
                i = i / j
        if i > 1:
            cur_primes_l.add(i)

        if cur_primes_l == primesL:
            numbers.add(cur_number)

    return [len(numbers), max(numbers)] if numbers != set() else []

