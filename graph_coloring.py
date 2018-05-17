import numpy as np


def promising(index, choice, W):
    for i in range(len(choice)):
        # TODO
        pass
    return True


def coloring(index, num_of_node, num_of_color, choice, W):
    if promising(index, choice, W):
        if index == num_of_node - 1:
            print(choice)
        else:
            for i in range(num_of_color):
                choice[index + 1] = i
                coloring(index + 1, num_of_color, num_of_node, choice)


if __name__ == '__main__':
    _W = np.array(
        [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 1, 0]])
    _num_of_node = 4
    _num_of_color = 3
    _choice = [0] * _num_of_node

   #coloring()
