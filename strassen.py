import numpy as np

def strassen(n, A, B):
    threshold = 32
    if n <= threshold:
        return A @ B

    A11 = np.array([[A[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])
    A12 = np.array([[A[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2))])
    A21 = np.array([[A[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), n)])
    A22 = np.array([[A[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2), n)])

    B11 = np.array([[B[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2))])
    B12 = np.array([[B[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2))])
    B21 = np.array([[B[rows][cols] for cols in range(int(n/2))] for rows in range(int(n/2), n)])
    B22 = np.array([[B[rows][cols] for cols in range(int(n/2), n)] for rows in range(int(n/2), n)])

    M1 = strassen(int(n/2), A11 + A22, B11 + B22)
    # TODO: M2 ..

    """
    M1 = (A11 + A22) @ (B11 + B22)
    M2 = (A21 + A22) @ B11
    M3 = A11 @ (B12 - B22)
    M4 = A22 @ (B21 - B11)
    M5 = (A11 + A12) @ B22
    M6 = (A21 - A11) @ (B11 + B12)
    M7 = (A12 - A22) @ (B21 + B22)
    """

