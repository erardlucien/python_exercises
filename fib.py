# write Fibonacci series up to n.
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# fib(2000)


# return Fibonacci series up to n
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)  # see below
        a, b = b, a + b
    return result


# fib100 = fib2(100)  call it
# print(fib100)  # write the result
