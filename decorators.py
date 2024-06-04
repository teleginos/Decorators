from math import sqrt


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print('Составное')
        else:
            flag = True
            for i in range(2, int(sqrt(result)) + 1):
                if result % i == 0:
                    flag = False
                    break
            if flag:
                print('Простое')
            else:
                print('Составное')
        return result
    return wrapper
