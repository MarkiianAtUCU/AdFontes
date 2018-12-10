from math import inf, floor



def greedy(a, b, mat, mis, ind):
    def S_stroke(i, j, d):
        return ((i+j)*mat/2) - d*(mat-mis)

    M = len(a)-1
    N = len(b)-1


    X = 2

    i = 0

    R = [[-inf for i in range(max(M, N) + 1)] for j in range(max(M, N) + 1)]
    T = [-inf for i in range(max(M, N) + 1)]

    while i < min(M, N) and a[i] == b[i]:
        i += 1

    R[0][0] = i
    T_stroke = S_stroke(i, i, 0)
    T[0] = T_stroke
    d = 0
    L = 0
    U = 0

    while L < U + 2:
        d += 1
        dprime = max(d - floor((X+mat/2) / (mat - mis)) - 1, 0)

        for k in range(max(0, L - 1), U+1):
            firstI = -inf
            secondI = -inf
            thirdI = -inf

            if L < k:
                firstI = R[d-1][k-1] + 1

            if L <= k <= U:
                secondI = R[d-1][k] + 1

            if k < U:
                thirdI = R[d-1][k+1]

            i = max(firstI, max(secondI, thirdI))

            j = i - k
            if i > -inf and S_stroke(i, j, d) >= T[dprime] - X:
                while i < M and j < N and a[i+1] == b[j+1]:
                    i += 1
                    j += 1

                R[d][k] = i
                T_stroke = max(T_stroke, S_stroke(i, j, d))
            else:
                R[d][k] = -inf

        T[d] = T_stroke

        for k in range(max(M, N)):
            if R[d][k] > -inf:
                L = k
                break

        for k in range(max(M, N), -1, -1):
            if R[d][k] > -inf:
                U = k
                break

        for k in range(max(M, N), -1, -1):
            if R[d][k] == N + k:
                L = max(L, k + 2)
                break

        for k in range(max(M, N)):
            if R[d][k] > -inf:
                U = min(U, k - 2)
                break

    return T_stroke
