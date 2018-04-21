import pdb

import numpy as np

V = ['a', 'b', 'c', 'd', 'e', 'f']
E = [
    ('a', 'b', 2), ('a', 'c', 3),
    ('b', 'c', 4), ('b', 'd', 1), ('b', 'e', 7),
    ('c', 'd', 3), ('c', 'e', 1),
    ('d', 'e', 2), ('d', 'f', 5),
    ('e', 'f', 4)
    ]

W = np.array(
    [[np.inf, 2, 3, np.inf, np.inf, np.inf],
     [2, np.inf, 4, 1, 7, np.inf],
     [3, 4, np.inf, 3, 1, np.inf],
     [np.inf, 1, 3, np.inf, 2, 5],
     [np.inf, 7, 1, 3, np.inf, 4],
     [np.inf, np.inf, np.inf, 5, 4, np.inf]])

def my_prim():
    """Spanning tree search algorithm.
    There are two groups. one is composed of passed vertices and the other is composed of not passed.
    1. Select the nearest vertex which belongs to not passed group.
    2. Check if the selected edge is suitable to current tree.
    3. Check if the tree which is added with selected vertex and edge is optimal.
    :return: None
    """
    n = len(V)

    min_cost = 0
    total_group = set(V)
    pass_group = set(['a'])
    no_pass_group = total_group - pass_group
    spanning_tree_edge_list = []

    for i in range(n-1):
        connected_node_list = []
        min_next_node = None
        min_edge = None
        min_dist = 987654321
        for vertex in pass_group:
            for edge in E:
                if edge[0] == vertex and edge[1] in no_pass_group:
                    connected_node_list.append(edge)
                    if min_dist > edge[2]:
                        min_next_node = edge[1]
                        min_edge = edge
                        min_dist = edge[2]
                elif edge[1] == vertex and edge[0] in no_pass_group:
                    connected_node_list.append(edge)
                    if min_dist > edge[2]:
                        min_next_node = edge[0]
                        min_edge = edge
                        min_dist = edge[2]
        if min_next_node is not None:
            pass_group.add(min_next_node)
            no_pass_group.remove(min_next_node)
            min_cost += min_dist
            spanning_tree_edge_list.append(min_edge)

    print("min_cost: ", min_cost)
    print(spanning_tree_edge_list)


def prim():
    n = len(V) 
    V_set = set(range(n))
    Y_set = set([0])
    F_set = set()
    min_cost = 0

    # nearest vertex in Y of each vertex involved in V - Y
    nearest = np.zeros([n], dtype=np.int32) 
    # nearest distacne to Y of each vertex involved in V - Y
    distance = np.zeros([n]) 

    # Start node is 0
    for i in range(n):
        nearest[i] = 0
        distance[i] = W[i][0] 
    distance[0] = -1

    # Repeat n-1
    for i in range(n-1):

        # Find nearest node involved in V - Y
        near_node = None
        min_dist = np.inf 
        for node in (V_set - Y_set):
            if 0 <= distance[node] < min_dist:
                min_dist = distance[node]
                near_node = node

        if near_node is None:
            print("Graph is not connected.")
            return

        # Add near_node to Y
        min_cost += distance[near_node]
        Y_set.add(near_node)
        F_set.add((nearest[near_node], near_node))
        distance[near_node] = -1

        # Update nearest, distance
        for node in (V_set - Y_set):
            if W[near_node][node] < distance[node]:
                distance[node] = W[near_node][node]
                nearest[node] = near_node

    print("min_cost: ", min_cost)
    print(F_set)


def kruskal():
    n = len(V)
    min_cost = 0
    F = []
    
    sorted_edge = sorted(E, key=lambda x: x[2])
    set_list = [set([i]) for i in V]

    def find_set_index(node):
        for index, each_set in enumerate(set_list):
            if node in each_set:
                return index
        return -1

    # Repeat n - 1
    while len(F) < n-1:
        min_edge = sorted_edge[0] 
        start_node = min_edge[0] 
        end_node = min_edge[1] 
        
        start_set_index = find_set_index(start_node)
        end_set_index = find_set_index(end_node)

        if start_set_index != end_set_index:
            set_list[start_set_index] = \
                    set_list[start_set_index] | set_list[end_set_index]
            del set_list[end_set_index]
            F.append(min_edge) 
            min_cost += min_edge[2]
        del sorted_edge[0]

    print("min_cost: ", min_cost)
    print(F)


if __name__ == '__main__':
    print("-- my_prim --")
    my_prim() 
    print("-- prim -- ")
    prim()
    print("-- kruskal --")
    kruskal()
