
def cost(a, b):
    if a == b:
        return match
    else:
        return mismatch


class Cell:
    def __init__(self, value, parents):
        self.value = value
        self.parents = parents

    def __repr__(self):
        return str(self.value)
    # return str(self.parents)


def NeedlemanWunsch(a, b, match, gap, mismatch):
    MATRIX = [[None for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

    for i in range(len(a) + 1):
        MATRIX[0][i] = Cell(i * gap, ["H"])

    for i in range(len(b) + 1):
        MATRIX[i][0] = Cell(i * gap, ["V"])

    MATRIX[0][0] = Cell(0, [])

    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            res = []

            # if MATRIX[i-1][j-1]!=None:
            res.append([MATRIX[i - 1][j - 1].value + match if a[j - 1] == b[i - 1] else mismatch, "D"])

            # if MATRIX[i-1][j]!=None:
            res.append([MATRIX[i - 1][j].value + gap, "V"])

            # if MATRIX[i][j-1]!=None:
            res.append([MATRIX[i][j - 1].value + gap, "H"])

            max_res = max(res, key=lambda x: x[0])
            parents = []

            for k in res:
                if k[0] == max_res[0]:
                    parents.append(k[1])

            MATRIX[i][j] = Cell(max_res[0], parents)
    return MATRIX


def backtrack(MATRIX, a, b):
    str_a = ""
    str_m = ""
    str_b = ""

    i = len(b)
    j = len(a)
    # pprint(MATRIX)
    sc = MATRIX[i][j]
    while MATRIX[i][j].parents != []:
        # print(i,j)
        if MATRIX[i][j].parents[0] == "D":
            i -= 1
            j -= 1
            str_a += a[j]
            str_b += b[i]
            if a[j] == b[i]:
                str_m += "|"
            else:
                str_m += "*"

        elif MATRIX[i][j].parents[0] == "H":
            j -= 1
            str_b += "-"
            str_a += a[j]
            str_m += " "

        else:
            i -= 1
            str_a += "-"
            str_b += b[i]
            str_m += " "

    return str_a[::-1] + "\n" + str_m[::-1] + "\n" + str_b[::-1] + "\n" + str(sc)


def NW(a, b, match = 1, gap = 0, mismatch = 0):
    return backtrack(NeedlemanWunsch(a, b, match, gap, mismatch), a, b)
