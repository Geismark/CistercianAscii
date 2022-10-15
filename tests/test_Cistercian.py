import unittest, json
from cistercian import Cistercian, CistercianNumeral

# TO RUN TESTS:
# ..\CistercianAscii> python -m pytest          <----- default
# ..\CistercianAscii> python -m pytest -q    <------ quiet (brief output) mode
# ..\CistercianAscii> python -m pytest tests    <------- use if issues using the previous two commands
# for (some) answers: https://stackoverflow.com/a/35896910

class TestCistercian():
	with open("tests/numeralTests.json", "r", encoding="utf-8") as f:
		numeral_json = json.load(f)

	def test_9999_numerals (self):
		for i in range(0, 10000):
			cist = CistercianNumeral(str(i))
			assert cist.arabic == str(i)
			assert cist.cistercian == self.numeral_json[i]
	
	def test_test_numerals (self):
		test_numerals = Cistercian.numeral_test()
		order = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999, 0000]
		for i in range(0, 10):
			assert test_numerals[i].cistercian == self.numeral_json[order[i]]
			assert int(test_numerals[i].arabic) == order[i]
			# FIXME 0000 rather than 0000 -> 0 (int)


# TODO section generation
# TODO main user inputs
# TODO random number generator?
# TODO print numeral
# TODO print arabic