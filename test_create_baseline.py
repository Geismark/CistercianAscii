from cistercian import CistercianNumeral, Cistercian

f_name = "tests/numeralTests.py"

def main(n):
	with open(f_name, "w") as fe:
		fe.write("")
		fe.close()

	for i in range(0, n+1):
		cist = CistercianNumeral(str(i))
		with open(f_name, "a", encoding='utf-8') as f:
			# encoding required for '‾' character: "UnicodeEncodeError: 'charmap' codec can't encode characters in position 52-54: character maps to <undefined>""
			cist_normal = [txt for txt in cist.cistercian] # doesn't work
			cist_replace = [txt.replace("‾", "\u203e") for txt in cist.cistercian] # doesn't work
			# print(f"{cist_replace=}")
			# numeral = [x.encode('utf-8') for x in cist_replace]
			# print(f"{numeral=}")
			f.write(f"t_{i} = {cist_normal}\n")
			f.close()

def second(n):
	with open(f_name, "r", encoding='utf-8') as f:
		content = f.readlines()
		# read nth line from the file
		result = content[n+1]
	# result2 = [codecs.decode(x, 'utf-8') for x in result]
	print(f"{result=}")
	

if __name__ == "__main__":
	main(100)
	second(3)