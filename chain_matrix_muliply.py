import numpy as np


def chain_multiply(M, D):
    n = D.shape[0] - 1
    M.fill(-1)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            M[i][j] = min(M[i][i+1] + M[i+2][j] + D[i] * D[i+1] * D[j])
            for k in range(i+2, j):
                M[i][j] = min(M[i][j], M[i][k] + M[k+1][j] + D[i] * D[j] * D[k])
    return M[1][n]


if __name__=='__main__':
    n = 3
    M = np.ones([n+1, n+1], dtype=np.int32)
    D = np.zeros([n+1], dtype=np.int32)
    D[0] = 10
    D[1] = 100
    D[2] = 5
    D[3] = 50
    print("minimum : ", chain_multiply(M, D))