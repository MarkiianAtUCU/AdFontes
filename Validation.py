import time
from random import randint
from NeedlemanWunsch import NW
from Greedy import greedy
from Bio import pairwise2
import random


def random_seq(len):
    return "".join([random.choice(["A", "T", "G", "C"]) for _ in range(len)]), "".join([random.choice(["A", "T", "G", "C"]) for _ in range(len)])


def validate(res1, res2):
    return int(res1.split("\n")[3]) == int(res2[2])


def get_data(data1, data2, l):
    f1 = open(data1, "r")
    f2 = open(data2, "r")
    a = ""
    b = ""

    for line in f1.readlines():
        a += line.strip()

    for line in f2.readlines():
        b += line.strip()

    start_point = randint(0, min(len(a), len(b) - l))

    if l < len(a) and l < len(b):
        return a[start_point:start_point+l], b[start_point:start_point+l]
    return 0, 0


def main(file1, file2, N_exp, Length):
    res_NW = []
    res_Bio = []
    res_Greedy = []
    for i in range(N_exp):
        two_seq = get_data(file1, file2, Length)

        now = time.time()
        res1 = NW(*two_seq, match, gap, mismatch)
        res_NW.append(time.time()-now)

        now = time.time()
        res2 = pairwise2.align.globalxx(*two_seq)[0]
        res_Bio.append(time.time()-now)

        now = time.time()
        res2 = greedy(*two_seq, match, mismatch, gap)
        res_Greedy.append(time.time()-now)

        if not validate(res1, res2):
            raise ValueError

    print(f"NW: For len {Length} time = {sum(res_NW)/len(res_NW)}")
    print(f"Biopython: For len {Length} time = {sum(res_Bio)/len(res_Bio)}")
    print(f"Biopython: For len {Length} time = {sum(res_Greedy)/len(res_Greedy)}")


N_exp = 10
Length = 500

match = 1
gap = 0
mismatch = 0
