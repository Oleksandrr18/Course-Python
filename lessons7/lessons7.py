# Task 1
def geometric_progression(q, n):
    x = q
    while True:
        yield x
        x *= n


gp = geometric_progression(1, 2)
for _ in range(60):
    print(next(gp))
# Task 2
def my_generator_analogue(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step == 0:
        raise ValueError("Not step in zero")
    connect = start
    if step > 0:
        while connect < stop:
            yield connect
            connect += step

    else:
        while connect > stop:
            yield connect
            connect += step


for i in my_generator_analogue(20, step=5):
    print(i)

# Task 3
def prime_numbers(limit):
    prime = [True] * (limit + 1)
    p = 2

    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False

        p += 1

    for p in range(2, limit + 1):
        if prime[p]:
            yield p


for pn in prime_numbers(40):
    print(pn)

# Task 4
def numbers():
    limit = 20
    for n in range(2, limit):
        n **= 3
        yield n


for num in numbers():
    print(num)


# Task 5
def fibonachi(n):
    first_number = 1
    second_number = 1
    index = 0
    while index <= n:
        num_numbers = first_number + second_number
        first_number = second_number
        second_number = num_numbers
        index = index + 1
        yield num_numbers
    return


for f in fibonachi(10):
    print(f)

# Task 6
from datetime import timedelta, datetime
def date(start, finish):
    s = start
    while s <= finish:
        yield s
        s += timedelta(days=1)


start = datetime(2024, 1, 1)
finish = datetime(2024, 12, 31)

for d in date(start, finish):
    print(d)






