from random import randrange


test_val = "1111222233334444555566667777888899990000"


def validate_numeral_input(number: str, multiple=False) -> str:
	if not isinstance(number, str):
		raise TypeError ("Cistercian input must be a string.")
	
	try:
		int(number)
	except ValueError:
		raise ValueError ("Cistercian input must be an integer.")
	
	if not multiple:
		if abs(int(number)) > 9999:
			raise ValueError ("Cistercian input cannot be longer than 4 digits long.")
	
	if abs(int(number)) != int(number):
		raise ValueError ("Cistercian input cannot be negative.")

	return number


def gen_random_number(single=False, max_digits: int = 40) -> str: # wanted a random number with more focus on randomness of number of digits

	if single and max_digits > 4: max_digits = 4
	digit_quantity = randrange(1, max_digits + 1)

	digit_list = [str(randrange(10)) for _ in range(1, digit_quantity + 1)]

	return "".join(digit_list)


def separate_values(input_value: str) -> list[str]:
	values = []

	while len(input_value) > 4:
		values.append(input_value[-4:])
		input_value = input_value[:-4]
	values.append(input_value)
	values.reverse()

	return values # in reverse order
