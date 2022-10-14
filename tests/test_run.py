# https://docs.pytest.org/en/stable/getting-started.html#our-first-test-run


# TO RUN TESTS:
# ..\CistercianAscii> python -m pytest          <----- default
# ..\CistercianAscii> python -m pytest -q    <------ quiet (brief output) mode
# ..\CistercianAscii> python -m pytest tests    <------- use if issues using the previous two commands
# for (some) answers: https://stackoverflow.com/a/35896910

from ..cistercian import CistercianNumeral


class TestCist:

	cist_val = "1"

	cist = CistercianNumeral(cist_val)
	
	def test_arabic(self):
		assert self.cist.arabic == self.cist_val
	
	def test_cistercian(self):
		print(f"------------\n{self.cist.cistercian}\n------------")
		assert 1 == 1


def test_print():
	print("-------------T1")

# def main(n):
# 	for i in range(0, n+1):
# 		cist = CistercianNumeral(str(i))
# 		print(f"{cist=}")
# 		# with open("numeralTests.py", "a") as f:	
# 		# 	return

# def test(): print("-------------T")

# def func(x):
# 	return x+1
# def test_answer():
# 	assert func(3) == 4