def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def main():
    print(factorial(10))
    print(factorial(30))


main()