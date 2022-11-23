def factorial(number):
    if number < 2:
        return 1
    return number * factorial(number-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))