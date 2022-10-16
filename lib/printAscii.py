def gen_print_ascii(numeral_list: list, print_arabic: bool) -> None:
	combined = [[] for _ in range(9)]
	for cistercian in numeral_list:
		numeral = cistercian.cistercian
		for row_index, numeral_row in enumerate(numeral):
			combined[row_index].append(numeral_row)
			combined[row_index].append("     ")
	for row in combined:
		hold = ""
		for block in row:
			hold = hold + block
		print(hold)
	if print_arabic:
		gen_print_arabic(numeral_list)
		

def gen_print_arabic(numeral_list: list) -> None:
	values = [cistercian.arabic for cistercian in numeral_list]
	extend = "".join([" " for _ in range(4 - int(len(str(values[0]))))])
	values[0] = extend + str(values[0])
	print(*values, sep="          ")

# FUTUREDO return printed text as strings?