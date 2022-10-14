import unittest, json
from cistercian import Cistercian, CistercianNumeral

# TO RUN TESTS:
# ..\CistercianAscii> python -m pytest          <----- default
# ..\CistercianAscii> python -m pytest -q    <------ quiet (brief output) mode
# ..\CistercianAscii> python -m pytest tests    <------- use if issues using the previous two commands
# for (some) answers: https://stackoverflow.com/a/35896910

class TestCistercian(unittest.TestCase):

	def test_9999_numerals (self):
		with open("tests/numeralTests.json", "r", encoding="utf-8") as f:
			numeral_json = json.load(f)
			
		for i in range(0, 10000):
			cist = CistercianNumeral(str(i))
			assert cist.cistercian == numeral_json[i]