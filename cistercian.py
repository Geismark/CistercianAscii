from lib.cistercianUtils import validate_numeral_input, separate_values, test_val, gen_random_number
from lib.genNumeral import gen_ascii
from lib.printAscii import gen_print_ascii, gen_print_arabic


class Cistercian:

	# N.B.: '-> list' will likely mean '-> list[CistercianNumeral]' 
	# FIXME couldn't get custom types in hints to work

	@staticmethod
	def get_numerals(input_value: str) -> list:
		values = separate_values(validate_numeral_input(input_value, multiple=True))
		numerals = [CistercianNumeral(val) for val in values]
		return numerals
	
	@staticmethod
	def print_numerals(numerals: list, print_arabic=True, separate=False) -> list:
		# FUTUREDO change separate to the print_ascii function?
		if not separate:
			gen_print_ascii(numerals, print_arabic)
			return
		for numeral in numerals:
			gen_print_ascii([numeral], print_arabic)
		return numerals # appears redundant, but makes other code cleaner

	@staticmethod
	def print_arabic(numerals: list) -> None: # actual print function is kept separate for DRY
		gen_print_arabic(numerals)
	
	@classmethod
	def print_arabic_to_cistercian(cls, input_value, print_arabic=True, separate=False) -> list: # ease of use, combines get and print, maybe a bit redundant but 
		return cls.print_numerals(cls.get_numerals(input_value), print_arabic=print_arabic, separate=separate)
	
	@classmethod
	def numeral_test(cls, print=True, print_arabic=True, separate=False) -> list:
		numerals = cls.get_numerals(test_val)
		if print:
			cls.print_numerals(numerals, print_arabic=print_arabic, separate=separate)
		return numerals

	@classmethod
	def get_random_numerals(cls, single_numeral=False, print=False, max_digits=40, print_arabic=True, separate=False) -> list:
		rand = gen_random_number(single=single_numeral, max_digits=max_digits)
		numerals = cls.get_numerals(rand)
		if print:
			cls.print_numerals(numerals, print_arabic=print_arabic, separate=separate)
		return numerals
		

class CistercianNumeral:
	def __init__ (self, input_value: str):
		self.arabic = validate_numeral_input(input_value) # arabic is an int stored as string
		self.cistercian = gen_ascii(self.arabic)
	
	def print_cistercian(self, print_arabic=True) -> None:
		gen_print_ascii([self], print_arabic)
	def print_arabic(self) -> None:
		gen_print_arabic([self])  # actual print function is kept separate for DRY


if __name__ == "__main__":
	Cistercian.get_random_numerals(print=True)
		