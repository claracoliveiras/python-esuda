number1 = 40
number2 = 60

common_divisor = 0

for i in range(1, number1 + 1):
    if number1 % i == 0 and number2 % i == 0:
        print(number1, number2, common_divisor)
        common_divisor = i

