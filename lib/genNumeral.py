from lib.numerals import h, d, numbers, stem, middle_row
import logging

# TODO rename 'glyph' to numeral

def gen_ascii(num: str) -> list: # takes len 1-4 string int and returns numeral in list[list[row]] format
	values = get_digits(num)
	glyph_top = []
	glyph_bottom = []
	ones, tens, hundreds, thousands = getSections(values)

	# top half
	for r in range(4):
		tens_list = [symbol for symbol in tens[r]]
		ones_list = [symbol for symbol in ones[r]]
		hold = tens_list + [stem[r]] + ones_list
		glyph_top.append("".join(hold))

	# bottom half (reversed to have rows go bottom-up)
	for r in reversed(range(4)):
		thousands_list = [symbol for symbol in thousands[r]]
		hundreds_list = [symbol for symbol in hundreds[r]]
		hold = thousands_list + [stem[-(r+1)]] + hundreds_list
		glyph_bottom.append("".join(hold))

	return glyph_top + [middle_row] + glyph_bottom


def get_digits(num: str) -> list[int]: # takes string int and returns int digits in list
	digits = [int(x) for x in list(str(num))[::-1]]
	digits.extend([0 for _ in range(0, 4 - min(4, len(str(num))))]) # inserts placeholder 0s for numeral gen
	return list(reversed(digits))


def getSections(values): # takes int for each section of numeral and gets appropriate strings
	ones = numbers[values[3]]

	tens = []
	for row in numbers[values[2]]:
		tens.append(list(reversed(row)))
	tens = replaceChars(tens, {d[0]:d[1]})

	hundreds = numbers[values[1]]
	hundreds = replaceChars(hundreds, {h[0]:h[1], d[0]:d[1]})

	thousands = []
	for row in numbers[values[0]]:
		thousands.append(list(reversed(row)))
	thousands = replaceChars(thousands, {h[0]:h[1]})

	return ones, tens, hundreds, thousands



def replaceChars(section, replace_dict): # takes strings for each section and ensures they are flipped appropriately per section
	out = []
	for r in section:
		row = "".join(r)
		for char in replace_dict:
			if char == h[0]:
				row2 = row.replace(char, replace_dict.get(char))
				if row2 == row:
					row2 = row.replace(replace_dict.get(char), char)
				row = row2
			elif char == d[0]:
				row2 = row.replace(char, replace_dict.get(char))
				if row2 == row:
					row2 = row.replace(replace_dict.get(char), char)
				row = row2
			else:
				row = row.replace(char, replace_dict.get(char))
				logging.debug(f"Replaced undefined characters:\n{replace_dict=}")
		out.append(list(row))
	return out