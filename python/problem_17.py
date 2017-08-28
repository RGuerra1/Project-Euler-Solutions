number = 5
def get_count_char(number):
	if number in [1,2,6,10]:
		return 3
	if number in [4,5,9]:
		return 4
	if number in [3,7,8,40, 50, 60]:
		return 5
	if number in [11,12,20,30,80,90]:
		return 6
	if number in [15,16,70,100]:
		return 7
	if number in [13,14,18,19]:
		return 8
	if number in [17]:
		return 9
	if number == 0:
		return 0
	return None

def get_count_char_under_100(number):
		first_digit = get_count_char(number%10)
		second_char = get_count_char((number/10)*10)
		print number, first_digit,second_char
		return first_digit + second_char

def get_count_number(number):
	if number <= 20:
		return get_count_char(number)
	print get_count_char(20)
	if number < 100:
		return get_count_char_under_100(number)
	if number < 1000:
		if number % 100 !=0:
			hundred_and = 10
		else:
			hundred_and = 7
		under_100 = get_count_char_under_100(number%100)
		hundres = get_count_char(number/100)
		total_char = hundred_and+hundres+under_100
		return total_char

def get_count_ten(number):
	total_sum = 0
	for i in range(1,number+1):
		total_sum += get_count_number(i)
	return total_sum

assert get_count_ten(5) == 19
assert get_count_number(90) == 6
assert get_count_number(99) == 10
assert get_count_number(342) ==23
assert get_count_number(115) == 20
print get_count_ten(99)
assert get_count_ten(19) == 106

assert get_count_ten(99) == 854
print get_count_ten(999) + 11