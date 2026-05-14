"""
Задание 1 Изоморфонсть
По времени O(n) n - длина строк
По памяти O(n) n - колв-во уникальных символов
"""
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    
    map_st = {}
    map_ts = {}

    for cs, ct in zip(s, t):
        if cs in map_st and map_st[cs] != ct:
            return False
        
        if ct in map_ts and map_ts[ct] != cs:
            return False
        
        map_st[cs] = ct
        map_ts[ct] = cs

    return True



"""
Задание 2 Натуралньая последовательность
По времени O(n) n - кол-во элементов
По памяти O(1)
"""
def missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    actual = sum(nums)

    return total - actual



"""
Задание 3 Факторизация
По времени O(sqrtn)
По памяти O(logn)
"""
def prime_factors(n):
    factors = []

    if n <= 1:
        return factors

    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    
    if n > 1:
        factors.append(n)
    
    return factors