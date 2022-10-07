from numerals import h, d, numbers, stem, middle_row



def getAscii(num): # TODO add user input
	values = getValues(num)
	glyph_top = []
	glyph_bottom = []
	ones, tens, hundreds, thousands = getSections(values)

	# top half
	for r in range(4):
		hold = []
		for s in tens[r]:
			hold.append(s)
		hold.append(stem[r])
		for s in ones[r]:
			hold.append(s)
		glyph_top.append("".join(hold))

	# bottom half (reversed to go top-down)
	for r in reversed(range(4)):
		hold = []
		for s in thousands[r]:
			hold.append(s)
		hold.append(stem[-(r+1)])
		for s in hundreds[r]:
			hold.append(s)
		glyph_bottom.append("".join(hold))

	return glyph_top + [middle_row] + glyph_bottom



def getValues(num):
	if len(str(num)) > 4: raise ValueError("Values input too large")
	values = [int(x) for x in list(str(num))[::-1]]
	values.extend([0 for _ in range(0, 4 - min(4, len(str(num))))])
	return list(reversed(values))



def getSections(values):
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



def replaceChars(section, replace_dict):
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
		out.append(list(row))
	return out