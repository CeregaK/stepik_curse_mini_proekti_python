# Посчитайте сколько "0" в конце факториала числа N.

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def trailing_zeros(n):
    m = factorial(n)
    zero = 0
    count = 0
    r = str(m)
    r = r[::-1]

    for i in r:
        if int(i) == zero:
            count += 1
        if int(i) != 0:
            break
    return count

print(f'{factorial(10):,}')
print(trailing_zeros(10))
