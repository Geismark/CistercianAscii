# TO RUN:
# ...\Cistercian> python -m unittest tests/test_run.py

import unittest, json
from cistercian import Cistercian, CistercianNumeral
from lib.genNumeral import gen_ascii, get_digits, get_sections, replace_chars
from lib.cistercianUtils import validate_numeral_input, gen_random_number, separate_values
from lib.printAscii import gen_print_ascii, gen_print_arabic
# TODO create tests for all functions(?)

class TestCistercianNumerals(unittest.TestCase):
	def setUp(self):
		print('\n') # in order to not cause issues with print tests displaying in terminal
		with open("tests/numeralTests.json", "r", encoding="utf-8") as f:
			self.numeral_json = json.load(f)

	def test_9999_numerals (self):
		for i in range(0, 10000):
			cist = CistercianNumeral(str(i))
			self.assertEqual(cist.arabic, str(i))
			self.assertEqual(cist.cistercian, self.numeral_json[i])
	
	def test_test_numerals (self):
		test_numerals = Cistercian.numeral_test()
		order = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 0000]
		for i in range(0, 10):
			self.assertEqual(test_numerals[i].cistercian, self.numeral_json[order[i]])
			self.assertEqual(int(test_numerals[i].arabic), order[i])
			# FIXME 0000 (str) rather than 0000 -> 0 (int)

class TestStringMethods(unittest.TestCase):

	def setUp(self):
		self.cist = CistercianNumeral("1")

	

if __name__ == '__main__':
	unittest.main()
	print("---------------SUCCESS")