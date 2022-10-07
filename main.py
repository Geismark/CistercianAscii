from genAscii import makeCistercian, genRandomNumber


def main():
	test_val = 1111222233334444555566667777888899990000
	p = True

	inp = input("Input a number: ")

	if inp in ["e", "exit", "c", "cancel"]:
		return None

	if inp in ["h", "help"]:
		print("Input 'h' for help, 't' for test, 'p' to disable arabic print, 'e' to exit")
		inp = input("Input a number: ")

	if inp in ["p", "print"]:
		p = False
		inp = input("Arabic print disabled, input a number: ")
	elif list(inp)[0] == "p":
		p = False
		inp = inp[1:]

	if inp in ["t", "test"]:
		return makeCistercian(test_val, p)
	elif inp in ["r", "rand", "random"]:
		return makeCistercian(genRandomNumber(), p)
	else:
		return makeCistercian(int(inp), p)


if __name__ == "__main__":
	main()
