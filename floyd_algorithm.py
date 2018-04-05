import numpy as np

def floyd_1(W, start, end):
    n = W.shape[0]
    D = np.copy(W)
    P = np.zeros(W.shape, dtype=np.int)
    P.fill(-1)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                    P[i][j] = k

    #print('W: ', W)
    #print('D: ', D)
    #print('P: ', P)
    return D[start][end], P


def reconstruct(P, start, end):
    #print("start : {}, end : {}".format(start, end))
    if P[start, end] != -1:
        reconstruct(P, start, P[start, end])
        print("v{} ->".format(P[start, end]), end=" ")
        reconstruct(P, P[start, end], end)
    return


if __name__=='__main__':
    weight = [[0, 1, np.inf, 1, 5],
             [9, 0, 3, 2, np.inf],
             [np.inf, np.inf, 0, 4, np.inf],
             [np.inf, np.inf, 2, 0, 3],
             [3, np.inf, np.inf, np.inf, 0]]
    W = np.array(weight)
    #print(W, W.shape)
    value, P = floyd_1(W, 4, 2)
    print("4 -> 2 : ", value)
    print("v4 ->", end=" ")
    reconstruct(P, 4, 2)
    print("v2 ")

