


def is_even_odd(n):
    if(n % 2 == 0):
        return "Even"
    else:
        return "Odd"

def is_positive_negative_zero(n):
    if(n > 0):
        return "Positive"
    elif(n < 0):
        return "Negative"
    else:
        return "Zero"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n %i == 0:
            return False
    return True

def is_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

def is_multiplication(n):
    for i in range(1,11     ):
        print(f"{n} * {i} = {n * i}")


print(is_even_odd(10))
print(is_even_odd(7))
print(is_positive_negative_zero(10))
print(is_positive_negative_zero(-9))
print(is_positive_negative_zero(0))
print(is_factorial(5))
print(is_multiplication(3))
