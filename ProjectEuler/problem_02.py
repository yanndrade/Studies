# URL = https://projecteuler.net/problem=2


def create_fibonacci_number(position):
    if position == 0:
        return 1
    elif position == 1:
        return 1

    else:
        return create_fibonacci_number(position-1) + create_fibonacci_number(position-2)

fib = 0
s = 0


fib = 0
i = 1
while fib < 4000000:

    fib = create_fibonacci_number(i)

    if fib%2 == 0:
        s = s + fib

    i += 1
