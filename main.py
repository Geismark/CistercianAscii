from lib.content_main import input_dict, input_other, help_print_text


def main(first=True) -> None:
	repeat = True
	delay_print = False
	
	if first:
		print(f"\n{help_print_text}")

	while repeat:
		inp = input("Input a number: ")
		other = True
		for input_list in input_dict:
			if inp in input_list:
				repeat, delay_print = input_dict[input_list](delay_print)
				other = False
				break
		if other:
			repeat, delay_print = input_other(delay_print, inp)
	print("\n-------- EXIT --------\n")



if __name__ == "__main__":
	main()


# FUTUREDO fix names, ascii/cistercian, etc.