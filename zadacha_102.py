# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def is_prime(n):
    if n == 1:
        return False
    for _ in range(2, n):
        if n % i == 0:
            return False
    return True


def factorize(n):
    factors = []
    num = 2
    while num * num <= n:  # перебираем простой делитель
        while n % num == 0:  # пока N на него делится
            n //= num  # делим N на этот делитель
            factors.append(num)
        num += 1
    if n > 1:
        factors.append(n)
    return factors


i = int(input())
if not is_prime(i):
    print(i, '=', ' x '.join(str(x) for x in factorize(i)))
else:
    print('число простое')
