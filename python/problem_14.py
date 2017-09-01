
calculate_values = {}
calculate_values[1] = 1


def calculate_serie(number):
    if number % 2 == 0:
        next_number = number / 2
    else:
        next_number = number * 3 + 1
    if next_number in calculate_values:
        return 1 + calculate_values[next_number]
    else:
        return 1 + calculate_serie(next_number)

max_value = 1
max_number = 1
for i in range(2, 1000000):
    serie_value = calculate_serie(i)
    if serie_value > max_value:
        max_number = i
        max_value = serie_value
    calculate_values[i] = serie_value

print max_number, max_value