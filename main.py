from decorators import is_prime


@is_prime
def sum_three(a, b, c):
    return a + b + c


if __name__ == '__main__':
    result = sum_three(2, 6, 6)
    print(result)
