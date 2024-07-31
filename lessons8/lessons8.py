# Task 1
def number_sequence(first_sub, n, progres_func):

    current_sub = first_sub
    for _ in range(n):
        yield current_sub
        current_sub = progres_func(current_sub)


def func(x):
    return x + 2


ns = number_sequence(1, 10, func)

for i in ns:
    print(i)

# Task 2
import time
def memoization(func):
    cache = {}

    def memoization_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoization_func


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Task 3
def arbitrary_function(numbers, func):
    num = [func(num) for num in numbers]

    return sum(num)


numbers = [1, 7, 8, 10, 6]
func = lambda x: x ** 2

gp = arbitrary_function(numbers, func)
print(gp)


memoization_fibo = memoization(fibonacci)

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    finish = time.time()
    return result, start - finish


n = 27

recursive_memo, recursive_time = measure_time(fibonacci, n)
print(f'Perspective approach:{recursive_memo}, Time:{recursive_time}')
result_memoization, time_memoization = measure_time(memoization_fibo, n)
print(f'Memoization approach{result_memoization}, Time:{time_memoization}')







