from cistercian import Cistercian
import logging


# all input tuples used later in input_dict
exit_inputs = ("e", "exit", "c", "cancel") # used in delay_arabic_print without "" to show arabic rather than exiting
empty_inputs = ("")
help_inputs = ("h", "help")
test_inputs = ("t", "test")
random_inputs = ("r", "rand", "random")
print_inputs = ("p", "print")


def delay_arabic_print(delay_print) -> bool: # bool: continue input while loop?
	if delay_print:
		i = input("Enter any input to see arabic numerals ")
		if i in exit_inputs:
			return False
	return True


def input_exit(delay_print) -> tuple[bool, bool]:
	logging.debug("direct input exit")
	return False, delay_print

def input_help(delay_print) -> tuple[bool, bool]:
	print("Input 'h' for help, 'e' to exit, 't' for test, 'r' for a random input, or 'p' to delay arabic print (e.g.: 'p123')")
	return True, delay_print

def input_test(delay_print) -> tuple[bool, bool]:
	numerals = Cistercian.numeral_test(print_arabic=False)
	output_continue = delay_arabic_print(delay_print)
	Cistercian.print_arabic(numerals)
	return output_continue, delay_print

def input_random(delay_print) -> tuple[bool, bool]:
	numerals = Cistercian.get_random_numerals(print=True, print_arabic=False)
	output_continue = delay_arabic_print(delay_print)
	Cistercian.print_arabic(numerals)
	return output_continue, delay_print
	
def input_delay(delay_print) -> tuple[bool, bool]:
	delay_print = not delay_print
	if delay_print: print("Arabic print will now be delayed.")
	else: print("Arabic print will not be delayed.")
	return True, delay_print

def input_other(delay_print, inp) -> tuple[bool, bool]:
	numerals = Cistercian.get_numerals(inp)
	Cistercian.print_numerals(numerals, print_arabic=False)
	output_continue = delay_arabic_print(delay_print)
	Cistercian.print_arabic(numerals)
	return output_continue, delay_print


# input_dict must come after functions are defined
input_dict = {
	empty_inputs:input_exit,
	exit_inputs:input_exit,
	help_inputs:input_help,
	test_inputs:input_test,
	random_inputs:input_random,
	print_inputs:input_delay,
}
