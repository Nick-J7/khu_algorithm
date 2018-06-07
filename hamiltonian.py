# -*- coding: utf-8 -*-

n = 5
W=[[0,1,1,0,1],[1,0,1,1,1],[1,1,0,1,0],[0,1,1,0,1],[1,1,0,1,0]]

def hamilton(index):
    #print(vindex)
    if promising(index):
        if index == n-1:
            print(vindex)
        else:
            for i in range(1, n):
                vindex[index + 1] = i
                hamilton(index + 1)

def promising(index):
#    if index == n-1:
#        print(index, vindex[index])
    if index == n-1 and W[vindex[index]][0] == 0:
        return False
    elif index != 0 and W[vindex[index]][vindex[index - 1]] == 0:
        return False
    for i in range(1, index):
        if vindex[i] == vindex[index]:
            return False
    return True

     
vindex = n * [0]
hamilton(0)
