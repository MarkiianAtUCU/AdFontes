import time
from NeedlemanWunsch import NW
from Bio import pairwise2
import random
def random_seq(len):
	return "".join([random.choice(["A","T","G","C"]) for _ in range(len)]), "".join([random.choice(["A","T","G","C"]) for _ in range(len)])


def validate(res1, res2):
	return int(res1.split("\n")[3])==int(res2[2])


N_exp = 10
Length = 500

res_NW = []
res_Bio = []

for i in range(N_exp):
	two_seq = random_seq(Length)
	now = time.time()
	res1 = NW(*two_seq)
	res_NW.append(time.time()-now)

	now = time.time()
	res2 = pairwise2.align.globalxx(*two_seq)[0]
	res_Bio.append(time.time()-now)
	if not validate(res1, res2):
		raise ValueError

print(f"NW: For len {Length} time = {sum(res_NW)/len(res_NW)}")
print(f"Biopython: For len {Length} time = {sum(res_Bio)/len(res_Bio)}")

