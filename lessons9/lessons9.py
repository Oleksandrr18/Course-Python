# Task 1
def my_decoration(func):
        def wrapper(*args, **kwargs):
            print('Action before calling a function')
            result = func(*args, **kwargs)
            print('Action after function call')

            return result

        return wrapper


@my_decoration
def my_d(job):
    print(f'My future job: {job}')


my_d('programmer')

# Task 3
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            print(f'Exception: {ex}')

    return wrapper


@handle_exceptions
def divide(a, b):
 return a/b

divide(5, 0)

# Task 4
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        total_time = start - end
        print(f' Time {total_time}')

        return result

    return wrapper


@measure_time
def some_function():
 time.sleep(2)

some_function()
print(some_function)
# Task 5
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def log_arguments_results(func):
    def wrapper(*args, **kwargs):
        logging.debug(f'Name func:{func.__name__}, arg: args:{args} kwargs:{kwargs}')
        res = func(*args, **kwargs)
        logging.debug(f'Name func:{func.__name__}, ras {res}')
        return res
    return wrapper


@log_arguments_results
def add_numbers(a, b):
 return a + b

add_numbers(3, 4)
# Task 6
def limit_calls(max_calls):
    def decorator(func):
        func.calls = 0

        def wrapper(*args, **kwargs):
            if func.calls >= max_calls:
                raise Exception(f'Error:{func.__name__}, max_calls:{max_calls}')
            func.calls += 1

            return func(*args, **kwargs)

        return wrapper

    return decorator


@limit_calls(3)
def some_function():
 print("Вызов функции")

some_function()
some_function()
some_function()
some_function()



