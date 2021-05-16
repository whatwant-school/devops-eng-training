# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 정의하기
def add_function(num1, num2):
    result = int(num1) + int(num2)
    return result


def subtract_function(num1, num2):
    result = int(num1) - int(num2)
    return result


def multiply_function(num1, num2):
    result = int(num1) * int(num2)
    return result


def division_function(num1, num2):
    result = int(num1) // int(num2)
    return result


def sqrt_function(num1):
    x = 2

    for idx in range(10):
        x = ( x + ( int(num1) / x ) ) / 2

    return x
