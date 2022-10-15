from lib.content_main import input_dict, input_other


def main() -> None:
	repeat = True
	delay_print = False

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
			# TODO print help rather than raise errors on erroneous input
	print("\n-------- EXIT --------\n")



if __name__ == "__main__":
	main()


# FUTUREDO fix names, ascii/cistercian, etc.