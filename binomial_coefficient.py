import numpy as np
import time

def binomial_slow(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return binomial_slow(n-1, k-1) + binomial_slow(n-1, k)

def binomial(n, k):
    C = np.zeros([n+1, k+1], dtype=np.int32)
    for i in range(n + 1):
        for j in range(min(i + 1, k + 1)):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]


if __name__=='__main__':

    print("C[3][2] = ", binomial(3, 2))
    print("C[5][2] = ", binomial(5, 2))
    n = 30
    k = 10
    s_time = time.time()
    value = binomial(n, k)
    e_time = time.time()
    print("fast C[{n}][{k}] = {value}".format(n=n, k=k, value=value))
    print("Elapsed time: {}".format(e_time - s_time))

    s_time = time.time()
    value = binomial_slow(n, k)
    e_time = time.time()
    print("slow C[{n}][{k}] = {value}".format(n=n, k=k, value=value))
    print("Elapsed time: {}".format(e_time - s_time))



