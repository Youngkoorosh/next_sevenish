def sum_of_digits(n):
    result = 0
    while n != 0:
        result += n % 10
        n //= 10

    return result

n = int(input())

n += 1
while sum_of_digits(n) % 7 != 0:
    n += 1

print(n)
