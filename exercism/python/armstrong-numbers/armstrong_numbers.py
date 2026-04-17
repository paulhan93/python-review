def is_armstrong_number(number) -> bool:
    temp = number
    digits = []
    while temp > 0:
        digit = temp % 10
        digits.append(digit)
        temp = temp // 10

    power = len(digits)
    armstrong_number = sum([x ** power for x in digits])
    return number == armstrong_number
