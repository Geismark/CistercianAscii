from cistercian import CistercianNumeral
import json

f_name = "numeralTests.json"

def gen_numeral_test_json(n):
	with open(f_name, "w", encoding='utf-8') as file_erase:
		file_erase.write("")
		file_erase.close()

	with open(f_name, "a", encoding='utf-8') as f:
		cist_hold = [[row for row in CistercianNumeral(str(i)).cistercian] for i in range(0, n+1)]
		cist_json = json.dumps(cist_hold)
		f.write(cist_json)
		f.close()

	# FUTUREDO separate lines per numeral in json file
	# FUTUREDO have single write?
	# TODO create single setup_test in source, move this to tests folder

# here as a reference, to be removed later:
# def read_numeral_test_json(n):
# 	with open(f_name, "r", encoding='utf-8') as f:
# 		content = json.load(f)

# 		for i in range(0, n+1):
# 			cist_numeral = CistercianNumeral(str(i)).cistercian
# 			if not content[i] == cist_numeral:
# 				print(f"{i=}: {content[i] == cist_numeral}")
			


	

if __name__ == "__main__":
	n = 9999
	gen_numeral_test_json(n)