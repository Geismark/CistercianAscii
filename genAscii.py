from random import randrange
from math import ceil
from genNumeral import getAscii



def makeCistercian(n, p):
	if not isinstance(n, int): raise TypeError("Input is not an integer")

	num_hold = n
	quant = ceil(len(str(n)) / 4)
	vals = []
	final = []

	for i in range(quant-1): # get 4-block values for all bar the final set of 4 digits
		vals.append(int(str(num_hold)[-4:]))
		num_hold = int(str(num_hold)[:-4])
	vals.append(num_hold)
	vals = vals[::-1] # reverse order, as took the values from right to left

	for i in range(quant):
		final.append(getAscii(vals[i]))

	if not p:
		printAscii(final, None)
	else:
		printAscii(final, vals)

	return final, vals



def printAscii(list, values):
	combined = [[] for _ in range(9)]
	for a in list:
		for ri, row in enumerate(a):
			combined[ri].append(row)
			combined[ri].append("     ")
	for row in combined:
		hold = ""
		for block in row:
			hold = hold + block
		print(hold)
	if values:
		extend = "".join([" " for _ in range(4 - int(len(str(values[0]))))])
		values[0] = extend + str(values[0])
	
		print(*values, sep="          ")



def genRandomNumber(d = 41):
	n = []
	digits = randrange(2, d)
	for _ in range(1, digits):
		n.append(str(randrange(10)))
	return int("".join(n))