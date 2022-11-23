def sum_numbers(number):
    if number < 1:
        return 0
    return number + sum_numbers(number-1)

print(sum_numbers(3))
print(sum_numbers(4))
print(sum_numbers(5))