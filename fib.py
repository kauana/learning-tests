def fib(number):
    if number == 0 or number == 1:
        return number
    return fib(number - 2) + fib(number - 1)

