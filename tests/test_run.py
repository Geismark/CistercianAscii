# TO RUN:
# ...\Cistercian> python -m unittest tests/test_run.py


import unittest, json
from cistercian import Cistercian, CistercianNumeral
from lib.genNumeral import gen_ascii, get_digits, get_sections, replace_chars
from lib.cistercianUtils import validate_numeral_input, gen_random_number, separate_values, test_val
from lib.printAscii import gen_print_ascii, gen_print_arabic
# TODO create tests for all functions(?)
# TODO main user inputs


function_print = False


class TestCistercianNumerals(unittest.TestCase):
	
	def setUp(self):
		function_print('\n') # in order to not cause issues with print tests displaying in terminal
		with open("tests/numeralTests.json", "r", encoding="utf-8") as f:
			self.numeral_json = json.load(f)

	def test_9999_numerals(self): # cistercian
		for i in range(0, 10000):
			cist = CistercianNumeral(str(i))
			self.assertEqual(cist.cistercian, self.numeral_json[i])
			self.assertEqual(cist.arabic, str(i))
	
	def test_test_numerals(self): # cistercian
		test_numerals = Cistercian.numeral_test(print=function_print)
		order = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 0000]
		for i in range(0, 10):
			self.assertEqual(test_numerals[i].cistercian, self.numeral_json[order[i]])
			self.assertEqual(int(test_numerals[i].arabic), order[i])
			# FIXME 0000 (str) rather than 0000 -> 0 (int)
		test_numerals_manual = Cistercian.get_numerals(test_val)
		self.assertEqual(len(test_numerals), len(test_numerals_manual))
		for n in range(0, len(test_numerals)):
			self.assertEqual(test_numerals[n].cistercian, test_numerals_manual[n].cistercian)
			self.assertEqual(test_numerals[n].arabic, test_numerals_manual[n].arabic)

	# genNumeral
	def test_gen_ascii(self):
		return NotImplemented


class TestGeneration(unittest.TestCase):
	def test_value_separation(self): # cistercianUtils
		return NotImplemented
	def test_gen_random_number(self): # cistercianUtils
		return NotImplemented
	def test_input_validation(self): # cistercianUtils
		return NotImplemented
	def test_get_digits(self): # genNumeral
		return NotImplemented
	def test_get_sections(self): # genNumeral
		return NotImplemented
	def test_replace_chars(self): # genNumeral
		return NotImplemented


class TestPrints(unittest.TestCase):
	def test_print_ascii(self): # printAscii
		return NotImplemented
	def test_print_arabic(self): # printAscii
		return NotImplemented
	



if __name__ == '__main__':
	unittest.main()
