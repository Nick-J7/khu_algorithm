""" N Queen Problem """
import numpy as np


n = 5
col = np.zeros(n)
is_found = False


def promising(index):
    result = True
    for i in range(index):
        if col[i] == col[index] or (abs(col[index] - col[i]) == index - i):
            result = False
            break
    return result


def backtracking(index):
    global is_found
    if is_found: return
    if index == -1 or promising(index):
        if index == n-1:
            print(col)
            #is_found = True
        else:
            for i in range(n):
                col[index + 1] = i
                backtracking(index + 1)


if __name__ == '__main__':
    col = np.zeros(n)
    is_found = False
    backtracking(-1)

