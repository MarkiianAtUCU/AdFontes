from pprint import pprint
match = 2
gap = -2
mismatch = -1


def cost(a,b):
	if a==b:
		return match
	return mismatch


class Cell:
	def __init__(self, value, parents):
		self.value = value
		self.parents = parents

	def __repr__(self):
		return str(self.value)

def NeedlemanWunsch(a,b):
	MATRIX = [[None for i in range(len(b)+1)] for i in range(len(a)+1)]
	MATRIX[0][0] = Cell(0, [])

	for i in range(1, len(a)+1):
		for j in range(1, len(b)+1):
			res = []

			if MATRIX[i-1][j-1]!=None:
				res.append([MATRIX[i-1][j-1].value + cost(a[i-1],b[j-1]), "D"])

			if MATRIX[i-1][j]!=None:
				res.append([MATRIX[i-1][j].value + gap, "V"])

			if MATRIX[i][j-1]!=None:
				res.append([MATRIX[i][j-1].value + gap, "H"])

			max_res = max(res, key = lambda x: x[0])
			parents = []

			for k in res:
				if k[0] == max_res[0]:
					parents.append(k[1])

			MATRIX[i][j] = Cell(max_res[0],parents)
	return MATRIX


def backtrack(MATRIX, a,b):
	str_a = ""
	str_m = ""
	str_b = ""

	i = len(a)
	j = len(b)
	# pprint(MATRIX)
	print("Score:", MATRIX[i][j])
	while MATRIX[i][j].parents!=[]:
		if MATRIX[i][j].parents[0]=="D":
			i-=1
			j-=1
			str_a+=a[i]
			str_b+=b[j]
			if a[i]==b[j]:
				str_m += "|"
			else:
				str_m += "*"
		elif MATRIX[i][j].parents[0]=="V":
			i-=1
			str_b += "-"
			str_a += a[i]
			str_m += " "

		else:
			j-=1
			str_a += "-"
			str_b += b[j]
			str_m += " "


	print(str_a[::-1]+"\n"+str_m[::-1]+"\n"+str_b[::-1])	





	# pprint(MATRIX)


a="CCGGTG"
b="CCT"
backtrack(NeedlemanWunsch(a, b),a ,b)
print("\n")

a="AAABBB"
b="BBBAAA"
backtrack(NeedlemanWunsch(a, b),a ,b)
print("\n")

a = "CTTCATAATCAAACCTGATCACAATTGGTTGTCAGTTTATTGGGGCGTATTTCAGAAAGTCCGGTTTCGGTTCTCTGTTTTTGTGGGAATATGATTACT"
b = "TATGTAATACTGCGTACGTGCATTGTAGGATATGACCGTCCTGACCGGCTTGCTTCACACCGGGCTTGCATCCGGCGACACGCCTACGTGCGGTTAGTA"
backtrack(NeedlemanWunsch(a, b),a ,b)


a = "ACCGT"
b = "ACG"
backtrack(NeedlemanWunsch(a,b),a,b)


a = "NLGPSTKDFGKISESREFDNQ"
b = "QLNQLERSFGKINMRLEDALV"
backtrack(NeedlemanWunsch(a,b),a,b)