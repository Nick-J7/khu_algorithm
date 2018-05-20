import numpy as np

import pdb


def promising(index, choice, W):
#    if index == -1:
#        return True
#    if index >= len(choice):
#        return False
    for i in range(index):
        if W[i][index] == 1 and choice[i] == choice[index]:
            return False
    return True

def coloring(index, num_of_node, num_of_color, choice, W):
    if promising(index, choice, W):
        if index == num_of_node - 1:
            #pdb.set_trace()
            print(choice)
        else:
            for i in range(num_of_color):
                choice[index + 1] = i + 1
                coloring(index + 1, num_of_node, num_of_color, choice, W)

if __name__ == '__main__':
    _W = np.array(
        [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]])
    _num_of_node = 4
    _num_of_color = 3
    _choice = [0] * _num_of_node

    coloring(-1, _num_of_node, _num_of_color, _choice, _W)
